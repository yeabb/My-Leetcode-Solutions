from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0]==1:
            return -1

        q=deque()
        q.append((0,0,1))
        visited=set()
        directions=[[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]

        while q:
           
            qLen=len(q)
            for i in range(qLen):
                cell=q.popleft()
                row, col, length = cell[0], cell[1], cell[2]
                
                if row ==len(grid)-1 and col==len(grid[0])-1:
                    return length

                nbrs=[]

                for rowDir, colDir in directions:
                    nbrRow=row+rowDir
                    nbrCol=col+colDir
                    if 0 <= nbrRow < len(grid) and 0 <= nbrCol < len(grid[0]) and grid[nbrRow][nbrCol]==0 and (nbrRow, nbrCol) not in visited:
                        nbrs.append((nbrRow, nbrCol, length+1))

                for nbr in nbrs:
                    visited.add((nbr[0], nbr[1]))
                    q.append(nbr)

        return -1



        