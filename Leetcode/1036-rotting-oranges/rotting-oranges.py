from collections import deque

class Solution:
    def orangesRotting(self, grid):
        m, n = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        queue = deque()
        fresh_count = 0
        
        # Step 1: Initialize queue and count fresh oranges
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))  # multi-source BFS
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0
        
        # Helper function
        def is_safe(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == 1
        
        # Step 2: BFS
        time = 0
        while queue:
            size = len(queue)
            
            for _ in range(size):
                i, j = queue.popleft()
                
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    
                    if is_safe(ni, nj):
                        grid[ni][nj] = 2
                        queue.append((ni, nj))
                        fresh_count -= 1
            
            time += 1
        
        return time - 1 if fresh_count == 0 else -1