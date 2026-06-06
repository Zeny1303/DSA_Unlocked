class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        lsum = 0
        left =[]
        left=[lsum]
        
        for i in range(len(nums)):
            lsum +=nums[i]# 10
            left.append(lsum) 
        rsum = 0
        new_right = []
# Iterate from the last index down to 0
        for i in range(len(nums) - 1, -1, -1):

            new_right.insert(0, rsum)
            rsum += nums[i]
        answer =[]
        for i in range(len(nums)):
            s = abs(left[i]-new_right[i])
            answer.append(s)
        return answer       
            
        