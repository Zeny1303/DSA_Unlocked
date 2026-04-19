class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxending = nums[0]
        minending = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            choice1 = nums[i]
            choice2 = nums[i]*minending
            choice3 = nums[i]*maxending
            maxending = max(choice1, max(choice2,choice3))
            minending = min(choice1, min(choice2,choice3))
            res = max(res, max(maxending,minending))
        return res    


        