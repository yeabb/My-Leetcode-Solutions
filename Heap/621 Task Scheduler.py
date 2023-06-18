import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count=collections.Counter(tasks)
        freq=[]
        for key, val in count.items():
            freq.append(-1*val)
        heapq.heapify(freq)
        
        q=collections.deque()
        time=0
        while freq or q:
            if q:
                if q[0][1]==time:
                    heapq.heappush(freq, q.popleft()[0])
                    continue
            if freq:
                curr=heapq.heappop(freq)+1
                if curr!=0:
                    q.append((curr, time+1+n))
                
            time+=1
        return time