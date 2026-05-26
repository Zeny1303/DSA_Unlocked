class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """

        # Sort by width ascending
        # If widths same -> height descending
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        heights = [h for w, h in envelopes]

        # Longest Increasing Subsequence on heights
        lis = []

        for h in heights:

            left = 0
            right = len(lis)

            while left < right:

                mid = (left + right) // 2

                if lis[mid] < h:
                    left = mid + 1
                else:
                    right = mid

            if left == len(lis):
                lis.append(h)
            else:
                lis[left] = h

        return len(lis)