class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(row, col):
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])
                    and (row, col) not in visited and grid[row][col]):
                return 0
            
            visited.add((row, col))
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

        visited=set()
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxArea = max(maxArea, dfs(i, j))

        return maxArea