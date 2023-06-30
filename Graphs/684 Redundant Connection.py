from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.roots=[i for i in range(n)]
        self.rank=[1]*n
    
    def find(self, x):
        if x==self.roots[x]:
            return x
        
        self.roots[x]=self.find(self.roots[x])
        return self.roots[x]

    def union(self,x,y):
        rootX, rootY = self.find(x),  self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.roots[rootY]=rootX
            elif self.rank[rootY] > self.rank[rootX]:
                self.roots[rootX] = rootY
            else:
                self.roots[rootY] = rootX
                self.rank[rootX]+=1
    def isConnected(self, x, y):
        return self.find(x) == self.find(y)



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        """
        here we are going to use spanning tree constructing algorithm
        in this specific example, we don't need minimum spanning tree, just a spanning tree so we are going to modify kruskal's algo and use it
        """
    
        vertices=set()
        for edge in edges:
            vertices.add(edge[0])
            vertices.add(edge[1])

        n=len(vertices)

        uf=UnionFind(n)

        countEdge=0
        dicludeEdge=[]
        for x, y in edges:
            if not uf.isConnected(x-1,y-1) and countEdge!=n-1:
                uf.union(x-1,y-1)
                countEdge+=1
            else:
                dicludeEdge.append([x,y])
            
            
        return dicludeEdge[-1]



        
