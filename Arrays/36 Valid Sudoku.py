class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for i in range(len(board)):
            setRow = set()
            setCol = set()
            for j in range(len(board[0])):

                if board[i][j] in setRow or board[j][i] in setCol:
                    return False
                else:
                    if board[i][j] != ".":
                        setRow.add(board[i][j]) 
                    if board[j][i] != ".":
                        setCol.add(board[j][i])
        
        dic = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i//3, j//3) in dic:
                    if board[i][j] in dic[(i//3, j//3)]:
                        return False
                    else:
                        if board[i][j] != ".":
                            dic[(i//3, j//3)].add(board[i][j])
                else:
                    if board[i][j] != ".":
                        dic[(i//3, j//3)] = set([board[i][j]])
        return True