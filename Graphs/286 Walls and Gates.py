from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        #Graph traversal problem
        #BFS

        q=deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if(rooms[i][j]==0):  #if gate
                    q.append((i,j))
        

        direction=[(0,-1),(-1,0),(0,1),(1,0)]
        dist=0
        while q:
            qlen=len(q)
            for i in range(qlen):
                row, col = q.popleft()

                nbrs=[]
                for i, j in direction:
                    if 0 <= row+i < len(rooms) and 0 <= col+j < len(rooms[0]) and rooms[row+i][col+j] == 2147483647:
                        nbrs.append((row+i, col+j))
                for nbr in nbrs:
                        q.append((nbr[0], nbr[1]))
                        rooms[nbr[0]][nbr[1]] = dist+1
            dist+=1
                    

                 

            

