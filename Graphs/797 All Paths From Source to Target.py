class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    
    
    #DFS recursive solution---------------------------------------
    
        def dfs(node):
            if node==n-1:
                res.append(path.copy())
                return

            for nextNode in graph[node]:
                path.append(nextNode)
                dfs(nextNode)
                path.pop()
            return
            
        n=len(graph)
        res=[]
        path=[0]
        dfs(0)
        return res

    #BFS iterative solution---------------------------------------------------
    
        # n=len(graph)
        # adjLst=defaultdict(list)
        # for i in range(n):
        #     for nbr in graph[i]:
        #         adjLst[i].append(nbr)
       
        # q=deque()
        # q.append([0])
        # res=[]
        # while q:
        #     qLen=len(q)
            
        #     for i in range(qLen):

        #         path=q.popleft()
        #         if path[-1]==n-1:
        #             res.append(path)
        #             continue
        #         for nbr in graph[path[-1]]:
        #             newPath=path.copy()
        #             newPath.append(nbr)
        #             q.append(newPath)
        # return res