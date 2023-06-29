class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(row, col):

            board[row][col]="A"
            nbrs=[]
            for i, j in direction:
                if 0 <= row+i < len(board) and 0 <= col+j < len(board[0]) and board[row+i][col+j]=="O":
                    nbrs.append((row+i, col+j))

            for nbr in nbrs:
                dfs(nbr[0], nbr[1])


        direction=[(0,-1),(-1,0),(0,1),(1,0)]
        
        for row in range(len(board)):
            if board[row][0]=="O":
                dfs(row, 0)
            if board[row][len(board[0])-1]=="O":
                dfs(row, len(board[0])-1)
         
        for col in range(len(board[0])):
            if board[0][col]=="O":
                dfs(0, col)
            if board[len(board)-1][col]=="O":
                dfs(len(board)-1, col)

        #Capture cells if there are any("O" to "X"") and revert the uncapturable cells from "A" back to "O"
        for i in range (len(board)):
            for j in range(len(board[0])):
                if board[i][j]=="O":
                    board[i][j]="X"
                if board[i][j]=="A":
                    board[i][j]="O"


#Similar Question in terms of approach is 417. Pacific Atlantic Water Flow