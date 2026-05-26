class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Add virtual balloons
        nums = [1] + nums + [1]

        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        # Length of interval
        for length in range(2, n):

            for left in range(0, n - length):

                right = left + length

                # Try every balloon as last burst
                for k in range(left + 1, right):

                    coins = (
                        nums[left] * nums[k] * nums[right]
                        + dp[left][k]
                        + dp[k][right]
                    )

                    dp[left][right] = max(dp[left][right], coins)

        return dp[0][n - 1]