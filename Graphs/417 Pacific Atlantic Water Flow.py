class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:


        def dfs(row,col, reachable):

            reachable.add((row, col))
            nbrs=[]
            for i, j in direction:
                if 0 <= row+i < len(matrix) and 0 <= col+j < len(matrix[0]) and (row+i, col+j) not in reachable and matrix[row+i][col+j]>=matrix[row][col]:
                    nbrs.append((row+i, col+j))
            for nbr in nbrs:
                dfs(nbr[0], nbr[1], reachable)

            


        direction=[(0,-1), (-1,0), (0,1), (1,0)]
        pacificReachable=set()
        atlanticReachable=set()

        for row in range(len(matrix)):
            dfs(row, 0, pacificReachable)
            dfs(row, len(matrix[0])-1, atlanticReachable)

        for col in range(len(matrix[0])):
            dfs(0, col, pacificReachable)
            dfs(len(matrix)-1, col, atlanticReachable)

        res=[]
        
        
        return list(pacificReachable.intersection(atlanticReachable))

        