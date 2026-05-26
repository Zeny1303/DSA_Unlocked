class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        m = len(dungeon)
        n = len(dungeon[0])

        # DP table
        dp = [[0] * n for _ in range(m)]

        # Bottom-right cell (princess cell)
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])

        # Last column
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(1, dp[i + 1][n - 1] - dungeon[i][n - 1])

        # Last row
        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = max(1, dp[m - 1][j + 1] - dungeon[m - 1][j])

        # Fill remaining cells
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):

                needed = min(dp[i + 1][j], dp[i][j + 1])

                dp[i][j] = max(1, needed - dungeon[i][j])

        return dp[0][0]
        