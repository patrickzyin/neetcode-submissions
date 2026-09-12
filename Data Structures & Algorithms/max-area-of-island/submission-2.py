class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        maxIslands = 0
        def dfs(grid, row, col, visited):
            if row < 0 or row >= rows or col < 0 or col >= cols or (row,col) in visited or grid[row][col] == 0:
                return 0
            visited.add((row,col))
            islandSum = 1
            for dr, dc in directions:
                islandSum += dfs(grid, dr + row, dc + col, visited)
            return islandSum

        ##OUTSIDE OF DFS
        for r in range(rows):
            for c in range(cols):
                area = dfs(grid, r,c, visited)
                maxIslands = max(area, maxIslands)
        return maxIslands