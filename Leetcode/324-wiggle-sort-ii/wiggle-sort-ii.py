class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        """

        nums.sort()

        n = len(nums)

        # Split into two halves
        half = (n + 1) // 2

        small = nums[:half][::-1]
        large = nums[half:][::-1]

        # Place smaller numbers at even indices
        nums[::2] = small

        # Place larger numbers at odd indices
        nums[1::2] = large
        