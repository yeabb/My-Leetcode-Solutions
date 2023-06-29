from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        edges=defaultdict(list)
        for u, v, w in times:                
            edges[u].append((w,v))

        visited=set()
        time=0
        minHeap=[[0,k]]
        while minHeap:              

            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue

            visited.add(n1)
            time=w1

            for w2, n2 in edges[n1]:
                heapq.heappush(minHeap, (w1+w2, n2))
        
        return time if len(visited) == n else -1


        #Runtime ---> O(E * log(V))
        #Space ----- O(E + V)
       