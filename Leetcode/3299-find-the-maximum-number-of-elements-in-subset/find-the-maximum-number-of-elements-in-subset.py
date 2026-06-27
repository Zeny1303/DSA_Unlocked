from collections import Counter
from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 1

        # Handle 1 separately
        if 1 in freq:
            if freq[1] % 2:
                ans = freq[1]
            else:
                ans = freq[1] - 1

        # Try every possible starting number
        for x in list(freq.keys()):
            if x == 1:
                continue

            length = 0
            cur = x

            while freq[cur] >= 2:
                length += 2
                cur *= cur

            if freq[cur] == 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans