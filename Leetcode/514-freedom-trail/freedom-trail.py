from collections import defaultdict

class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        n = len(ring)

        positions = defaultdict(list)
        for i, ch in enumerate(ring):
            positions[ch].append(i)

        memo = {}

        def dp(ring_pos, key_pos):
            if key_pos == len(key):
                return 0

            if (ring_pos, key_pos) in memo:
                return memo[(ring_pos, key_pos)]

            ans = float('inf')

            for next_pos in positions[key[key_pos]]:
                diff = abs(next_pos - ring_pos)
                rotate = min(diff, n - diff)

                ans = min(
                    ans,
                    rotate + 1 + dp(next_pos, key_pos + 1)
                )

            memo[(ring_pos, key_pos)] = ans
            return ans

        return dp(0, 0)