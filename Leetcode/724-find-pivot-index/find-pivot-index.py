class Solution(object):
    def pivotIndex(self, nums):
        t=0
        left_sum=0
        for i in range(len(nums)):
            t+=nums[i]
        for i in range(len(nums)):
            
            
            # Sum of everything strictly to the right
            right_sum = t - left_sum -  nums[i]
            
            if left_sum == right_sum:
                return i
            # Sum of everything strictly to the left
            left_sum += nums[i]     
        return -1