class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total_subarrays = 0
        
        # Iterate over all possible starting points of the subarray
        for i in range(n):
            target_count = 0
            
            # Expand the subarray from index i to j
            for j in range(i, n):
                if nums[j] == target:
                    target_count += 1
                
                length = j - i + 1
                
                # Check if target is strictly more than half of the subarray length
                if target_count > length // 2:
                    total_subarrays += 1
                    
        return total_subarrays