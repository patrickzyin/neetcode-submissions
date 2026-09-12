class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows, cols = len(grid), len(grid[0])
        islands = 0 
        def dfs(grid, row, col, visited):
            if row < 0 or row >= rows or col < 0 or col >= cols or (row,col) in visited or grid[row][col] == "0":
                return
            visited.add((row,col))
            for dr, dc in directions:
                dfs(grid, dr + row, dc + col, visited)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(grid, r,c, visited)
                    islands += 1
        return islands