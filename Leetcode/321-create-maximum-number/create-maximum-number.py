class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """

        def max_subsequence(nums, k):

            stack = []

            drop = len(nums) - k

            for num in nums:

                while stack and drop > 0 and stack[-1] < num:

                    stack.pop()
                    drop -= 1

                stack.append(num)

            return stack[:k]

        def merge(seq1, seq2):

            result = []

            while seq1 or seq2:

                # Lexicographically larger sequence wins
                if seq1 > seq2:
                    result.append(seq1.pop(0))
                else:
                    result.append(seq2.pop(0))

            return result

        best = []

        # Try all splits
        for i in range(k + 1):

            if i <= len(nums1) and (k - i) <= len(nums2):

                part1 = max_subsequence(nums1, i)

                part2 = max_subsequence(nums2, k - i)

                candidate = merge(part1[:], part2[:])

                best = max(best, candidate)

        return best