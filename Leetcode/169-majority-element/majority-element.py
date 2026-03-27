class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        f={}
        n=len(nums)
        for i in range(n):
            f[nums[i]] =f.get(nums[i],0)+1
        t = n/2
        for key,values in f.items():
            if values > t:
                return key
        