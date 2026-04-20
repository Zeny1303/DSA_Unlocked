class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxending = nums[0] #2
        minending = nums[0]
        resmax = nums[0]#2
        resmin = nums[0]
        for i in range(1,len(nums)):
            choice1 = nums[i] # i=1 -> -5
            choice2 = nums[i]+maxending # i=2 -> -5+2 = -3
            choice3 = nums[i]+minending
            maxending = max(choice1,max(choice2,choice3))
            resmax = max(resmax,maxending)
            minending = min(choice1,min(choice2,choice3))
            
            resmin=min(resmin,minending)
        return max(resmax,abs(resmin))  