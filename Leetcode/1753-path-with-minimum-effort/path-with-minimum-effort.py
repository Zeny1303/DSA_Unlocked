import heapq

class Solution(object):
    def minimumEffortPath(self, heights):
        n = len(heights)
        m = len(heights[0])
        
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        # distance matrix
        distance = [[float('inf')] * m for _ in range(n)]
        distance[0][0] = 0

        pq = [(0, 0, 0)]  # (effort, x, y)

        while pq:
            effort, x, y = heapq.heappop(pq)

            # 🔥 important optimization
            if effort > distance[x][y]:
                continue

            for k in range(4):
                ii = x + dx[k]
                jj = y + dy[k]

                if ii < 0 or jj < 0 or ii >= n or jj >= m:
                    continue

                new_dist = max(effort, abs(heights[x][y] - heights[ii][jj]))

                if new_dist < distance[ii][jj]:
                    distance[ii][jj] = new_dist
                    heapq.heappush(pq, (new_dist, ii, jj))

        return distance[n - 1][m - 1]