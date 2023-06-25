from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        fresh=0
        q=deque()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    fresh+=1            #find out the total number of fresh oranges
                if grid[i][j]==2:
                    q.append((i,j))     #add the rotten ones into the queue
       
        direction=[(0,-1), (-1,0), (0,1), (1,0)]
        time=0
        while q and fresh>0:

            qLen=len(q)
            for i in range(qLen):      
                cell = q.popleft()
                row, col = cell[0], cell[1]
                    
                nbrs=[]
                for rowDir, colDir in direction:
                    nbrRow, nbrCol = row+rowDir, col+colDir
                    
                # check if the neighbour coordinate is inbound and it hold fresh oranges
                    if 0 <= nbrRow < len(grid) and 0 <= nbrCol < len(grid[0]) and grid[nbrRow][nbrCol]==1:
                        nbrs.append((nbrRow, nbrCol))

                for nbr in nbrs:
                    grid[nbr[0]][nbr[1]]=2    #mark the current fresh oranges as rotten
                    fresh-=1
                    q.append(nbr)       #append the new rotten coordinates to the queue

            time+=1     #increment the time only after finishing one whole level

        return time if fresh==0 else -1     #return the time if there are no fresh oranges left else return -1

