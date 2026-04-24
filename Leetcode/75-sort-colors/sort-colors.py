class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        low = 0
        mid = 0
        high = n - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Case 0: Swap to the front
                nums[mid], nums[low] = nums[low], nums[mid]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # Case 1: Already in the middle
                mid += 1
            else:
                # Case 2: Swap to the back
                nums[mid], nums[high] = nums[high], nums[mid]
                # CRITICAL: Do not increment mid here!
                high -= 1