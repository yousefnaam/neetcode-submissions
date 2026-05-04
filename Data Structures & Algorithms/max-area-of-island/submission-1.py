from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        #traversing, if we reach a 1, we will call our traversal algorithm on it,
        #append to queue, mark it as visited, append neighbors to queue, check to see if it is valid,
        #in bounds (not less than 0 or >= len) also its a 1

        maxarea = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    maxarea = max(maxarea, self.bfs(grid, row, col))
        return maxarea


    def bfs(self, grid, row,col):
        area = 0
        queue =  deque([(row,col)])
        grid[row][col]= 0
        while queue: 
            r,c = queue.popleft()
            area += 1

            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            for dx, dy in directions:
                if self.notvalid(grid, dx + r, dy + c):
                    continue
                grid[dx + r][dy + c] = 0
                queue.append((dx + r, dy + c))
        return area
                    



    def notvalid(self, grid,row,col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
            return True
        return False
        
                    


        