from collections import defaultdict, deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

#DFS Iterative Implementation--------------------------------------------------
    
        graph=defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])


        stack=[source]
        visited=[False]*n
        visited[source]=True

        while stack:
            parent=stack.pop()

            for Nextnode in graph[parent]:
                if Nextnode == destination:
                    return True
                if not visited[Nextnode]:
                    visited[Nextnode]=True
                    stack.append(Nextnode)

        return visited[destination]
    
    
#BFS Iterative Implementation------------------------------------------------------------

        # graph=defaultdict(list)
                
        #         for edge in edges:
        #             graph[edge[0]].append(edge[1])
        #             graph[edge[1]].append(edge[0])
                
        #         q=deque()
        #         q.append(source)
        #         visited=set()
        #         visited.add(source)
        #         while q:
        #             qLen=len(q)
        #             for i in range(qLen):
        #                 parent=q.popleft()
        #                 if parent==destination:
        #                     return True
        #                 for nbr in graph[parent]:
        #                     if nbr not in visited:
        #                         visited.add(nbr)
        #                         q.append(nbr)
                            
        #         return False