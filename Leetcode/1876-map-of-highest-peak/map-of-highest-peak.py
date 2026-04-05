class Solution(object):
    def highestPeak(self, isWater):
        """
        :type isWater: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(isWater)
        n = len(isWater[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        height = [[-1 for _ in range(n)] for _ in range(m)]
        # queue initiate 
        queue = deque()
        
        # traversal on grid 
        for i in range(m):
            for j in range(n):
                if isWater[i][j]==1:
                    # yahi water hai toh uska height = 0 hoga 
                    height[i][j]=0
                    queue.append((i,j))
        # Helper function
        def is_safe(x, y):
            return 0 <= x < m and 0 <= y < n and height[x][y]== -1
        # Khandani code - multi source BFS template 
        while queue:
            size = len(queue)
            for _ in range(size):
                i,j = queue.popleft()
                for dx,dy in directions:
                    ii,jj = i+dx, j+dy
                    if is_safe(ii,jj):
                        height[ii][jj] = height[i][j]+1
                        queue.append((ii,jj))
        return height                 

        