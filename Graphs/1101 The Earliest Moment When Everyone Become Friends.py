class UnionFind:
    def __init__(self, n):
        self.roots=[i for i in range(n)]
        self.rank=[1]*n
        self.count=n
        
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
            if self.rank[rootY] > self.rank[rootX]:
                self.roots[rootX] = rootY
            else:
                self.roots[rootY] = rootX
                self.rank[rootX]+=1
            self.count-=1
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        
        uf=UnionFind(n)
        
        logs.sort()
        for log in logs:
            uf.union(log[1], log[2])
            if uf.count==1:
                return log[0]
        
        return -1