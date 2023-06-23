from collections import defaultdict
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        def dfs(node):
            if not graph[node]:
                if node==destination:
                    return True
                else:
                    return False

            visited.add(node)
            cycle=False
            for nbr in graph[node]:
                if nbr in visited:
                    if not graph[nbr] or (graph[nbr] and nbr==node):
                        return False
                    else:
                        cycle=True
                        continue

                if not dfs(nbr):
                    return False
                    
            if len(graph[node])==1 and cycle:
                return False
            return True


        graph=defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
        visited=set()
        return dfs(source)