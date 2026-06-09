class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        low =0
        high = len(nums)-1
        l=0
        h=len(nums)-1
        fo=-1
        eo=-1
        # first occurenece dudh na hai
        while low<=high:
            mid = (low+high)//2 # 2
            if nums[mid] == target:
                fo = mid 
                high = mid -1
                
            elif nums[mid]>target:
                high=mid-1
            else:
                low =mid+1  
        while l<=h:
            mid = (l+h)//2 # 2
            if nums[mid] == target:
                eo = mid 
                l = mid +1
                
            elif nums[mid]>target:
                h=mid-1
            else:
                l =mid+1                 

        return [fo,eo]
        