class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        max_reach = 0

        for i in range(len(nums)):

            # if current index is unreachable
            if i > max_reach:
                return False

            # update farthest reachable index
            max_reach = max(max_reach, i + nums[i])

        return True