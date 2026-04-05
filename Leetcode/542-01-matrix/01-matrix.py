
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(mat)
        n = len(mat[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        distance = [[-1 for _ in range(n)] for _ in range(m)]

        queue = deque()

        # traversal over grids
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    distance[i][j]=0
                    queue.append((i,j))

        def is_safe(x, y):
            return 0 <= x < m and 0 <= y < n and distance[x][y]== -1 # means unvisited hai 
        while queue:
            size = len(queue)
            for _ in range(size):
                i,j = queue.popleft()
                for dx,dy in directions:
                    ii,jj = i+ dx,j+dy 
                    if is_safe(ii,jj):
                        distance[ii][jj] = distance[i][j]+1
                        queue.append((ii,jj))
        return distance                               
        
        