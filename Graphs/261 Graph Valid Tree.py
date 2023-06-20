class UnionFind:

    def __init__(self, n):

        self.rank = [1]*n
        self.count=0
        self.res=True
        self.roots = [0]*n
        for i in range(n):
            self.roots[i]=i
            
    def find(self, x):

        if x==self.roots[x]:
            return x
        
        self.roots[x]=self.find(self.roots[x])
        return self.roots[x]
    
    def union(self, x, y):

        rootX, rootY=self.find(x), self.find(y)
        
        if rootX != rootY:

            if self.rank[rootX] > self.rank[rootY]:
                self.roots[y] = rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.roots[x] = rootY
            else:
                self.roots[y] = rootX
                self.rank[rootX]+=1
            return True

        else:
            return False
        
            


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if n==0:
            return False

        if len(edges) != n-1:
            return False
        
        uf=UnionFind(n)
        
        for edge in edges:

            if not uf.union(edge[0], edge[1]):
                return False
        
        return True