from collections import defaultdict

class UnionFind:

    def __init__(self, n):
        self.roots=[i for i in range(n)]
        self.rank=[0]*n
        

    def find(self,x):
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

    def isConnected(self, x, y):
        return self.find(x)==self.find(y)


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges=[]
        
        for i in range(len(points)-1):       # this gonna take N^2 time - for N points
            for j in range(i+1, len(points)):
                x1,x2=points[i][0], points[j][0]
                y1,y2=points[i][1], points[j][1]
                dis=abs(x2-x1) + abs(y2-y1)
                edges.append((dis, (x1,y1), (x2,y2)))
        
        edges.sort()            #O(N^2 log (N^2) )       since we have "N^2" edges

        dic=defaultdict(int)
        for i in range (len(points)):     #O(N)
            dic[tuple(points[i])]=i
        
        
        uf=UnionFind(len(points))
        minCost=0
        countEdges=0
        for dis, point1, point2 in edges:      #O(N^2 * α(N))
            if not uf.isConnected(dic[point1], dic[point2]):
                uf.union(dic[point1], dic[point2])
                countEdges+=1
                minCost+=dis
                if countEdges==len(points)-1:
                    break

        return minCost

        #Time Complexity --- O(N^2 + N^2 log(N^2) + N + N^2 * α(N))
        #                ----O(N^2 log(N^2)) = O(N^2 log(N))     
        #Space Complexity ---- O(N^2)          

