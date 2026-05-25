class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        jumps = 0
        current_end = 0
        farthest = 0

        # No need to process last index
        for i in range(len(nums) - 1):

            # Farthest reachable index
            farthest = max(farthest, i + nums[i])

            # End of current jump range
            if i == current_end:

                jumps += 1
                current_end = farthest

        return jumps