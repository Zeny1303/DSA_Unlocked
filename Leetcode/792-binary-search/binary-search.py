class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low =0
        high=len(nums)-1
        while low<= high:
            ans = (low + high) //2
            if nums[ans] == target :
                return ans
            elif nums[ans]>target:
                high-=1
            else:
                low +=1
        return -1                