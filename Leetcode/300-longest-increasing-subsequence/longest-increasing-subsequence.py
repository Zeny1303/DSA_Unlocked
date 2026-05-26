class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        tails = []

        for num in nums:

            left = 0
            right = len(tails)

            # Binary search
            while left < right:

                mid = (left + right) // 2

                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid

            # Extend LIS
            if left == len(tails):
                tails.append(num)

            # Replace existing value
            else:
                tails[left] = num

        return len(tails)