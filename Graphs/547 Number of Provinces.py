class UnionFind:
    def __init__(self, numOfNodes):
        
        self.roots=[0]*numOfNodes
        self.rank=[1]*numOfNodes
        self.count=numOfNodes
        for i in range(len(self.roots)):
            self.roots[i]=i

    def find(self, x):

        if x==self.roots[x]:
            return x
        self.roots[x]=self.find(self.roots[x])
        return self.roots[x]

    def union(self, x, y):

        rootX, rootY=self.find(x), self.find(y)

        if rootX!=rootY:
            if self.rank[rootX]>self.rank[rootY]:
                self.roots[rootY]=rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.roots[rootX]=rootY
            else:
                self.roots[rootX]=rootY
                self.rank[rootY]+=1
            self.count-=1
       
class Solution:
                    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if len(isConnected)==0:
            return 0
        uf=UnionFind(len(isConnected))
        
        for row in range(len(isConnected)):
            for col in range(row+1, len(isConnected)):
                if isConnected[row][col]==1:
                    uf.union(row, col)
       
        
        return uf.count
       
                