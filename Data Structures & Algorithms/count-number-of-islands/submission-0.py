from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        if not grid or not grid[0]:
            return 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += self.bfs(grid,row,col)
        
        return count


    def bfs(self, grid, row, col):
        queue = deque([(row,col)])
        while queue:
            r,c = queue.popleft()
            if self.notvalid(grid, r, c):
                continue
            grid[r][c] = "0"

            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            for dr,dc in directions:
                queue.append((r+dr, c+dc))
        return 1
                
    def notvalid(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
            return True







        