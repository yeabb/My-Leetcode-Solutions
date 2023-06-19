class Solution:

    def __init__(self):
        self.output=False
    def exist(self, board: List[List[str]], word: str) -> bool:

        def findStartCells():
            startCells=[]
            for i in range(n):
                for j in range(m):
                    if board[i][j]==word[0]:
                        startCells.append((i,j))
            return startCells
    

        def backTracking(start, indx):
           
            if indx==len(word):
                return True
            

            nbrs=[]
            left=(start[0], start[1]-1)
            top=(start[0]-1, start[1])
            right=(start[0], start[1]+1)
            bottom=(start[0]+1, start[1])
            if left[1]>=0 and (left[0], left[1]) not in visited:
                nbrs.append(left)
            if top[0]>=0 and (top[0], top[1]) not in visited:
                nbrs.append(top)
            if right[1]<m and (right[0], right[1]) not in visited:
                nbrs.append(right)
            if bottom[0]<n and (bottom[0], bottom[1]) not in visited:
                nbrs.append(bottom)

            visited.add((start[0], start[1]))
            
            for cell in nbrs:
                if board[cell[0]][cell[1]]==word[indx]:
                    if backTracking(cell, indx+1):
                        return True
                    
            visited.remove((start[0], start[1]))
            return False




        n=len(board)
        m=len(board[0])
        startCells=findStartCells()
        visited=set()
        for start in startCells:
            if backTracking(start, 1):
                return True
           
            
        return False 
