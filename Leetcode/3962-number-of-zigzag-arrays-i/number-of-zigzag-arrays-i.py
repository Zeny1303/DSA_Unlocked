class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        
        # If the length is 1, any value in the range [l, r] is valid
        if n == 1:
            return (r - l + 1) % MOD
            
        # Map values from [l, r] to 0-indexed array of size M
        M = r - l + 1
        
        # dp[0][x]: ending at x, next move must be DOWN (< x)
        # dp[1][x]: ending at x, next move must be UP (> x)
        dp0 = [1] * M
        dp1 = [1] * M
        
        # Iterate for the remaining elements from length 2 to n
        for i in range(2, n + 1):
            next_dp0 = [0] * M
            next_dp1 = [0] * M
            
            # To optimize transitions:
            # next_dp0[y] needs sum of dp1[x] for x > y (suffix sum)
            # next_dp1[y] needs sum of dp0[x] for x < y (prefix sum)
            
            # 1. Compute prefix sums of dp0 to quickly get sum(dp0[x]) for x < y
            pref_dp0 = 0
            for y in range(M):
                next_dp1[y] = pref_dp0
                pref_dp0 = (pref_dp0 + dp0[y]) % MOD
                
            # 2. Compute suffix sums of dp1 to quickly get sum(dp1[x]) for x > y
            suff_dp1 = 0
            for y in range(M - 1, -1, -1):
                next_dp0[y] = suff_dp1
                suff_dp1 = (suff_dp1 + dp1[y]) % MOD
                
            dp0 = next_dp0
            dp1 = next_dp1
            
        # The total answer is the sum of all valid configurations of length n
        return (sum(dp0) + sum(dp1)) % MOD