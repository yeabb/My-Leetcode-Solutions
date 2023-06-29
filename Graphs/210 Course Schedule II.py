from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        def dfs(crs):
            if crs in visited:
                return True

            if crs in checkCycle:
                return False
        
            
            checkCycle.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            checkCycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        


        adj=defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)


        visited=set()
        checkCycle=set()
        res=[]
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res