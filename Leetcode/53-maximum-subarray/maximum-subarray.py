class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxending = nums[0]
        result = nums[0]
        for i in range(1,len(nums)):
            choice1 = nums[i]
            choice2 = nums[i]+maxending
            maxending=max(choice1,choice2)
            result = max(maxending,result)
        return result    
        