from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

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
            return True 



        adj=defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        checkCycle=set()
        visited=set()
        for crs in range(numCourses):
            if not dfs(crs):
                return False
            
        return True
            
        
        