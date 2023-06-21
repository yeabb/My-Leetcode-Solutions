class UnionFind:
    def __init__(self, n):
        self.roots=[i for i in range(n)]
        self.rank=[1]*n
        
    def find(self, x):
        if x==self.roots[x]:
            return x
        
        self.roots[x]=self.find(self.roots[x])
        return self.roots[x]
    
    def union(self, x, y):
        
        rootX, rootY = self.find(x), self.find(y)
        if rootX != rootY:
            
            if self.rank[rootX] > self.rank[rootY]:
                self.roots[rootY] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.roots[rootX] = rootY
            else:
                self.roots[rootY] = rootX
                self.rank[rootX]+=1

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:

        n=len(s)
        uf=UnionFind(n)
        dic={}
        
        for pair in pairs:
            uf.union(pair[0], pair[1])

        for i in range(n):
            root=uf.find(i)
            if root in dic:
                dic[root].append(s[i])
            else:
                dic[root]=[s[i]]
            
        for key in dic:
            dic[key]=sorted(dic[key], reverse=True)
            
        output=""
        for i in uf.roots:
            char=dic[i].pop()
            output+=char

        return output
        