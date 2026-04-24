class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # Initialize with the sum of the first triplet
        closest_sum = nums[0] + nums[1] + nums[2] # -4
        
        for i in range(len(nums) - 2):
            # Optional: skip duplicate i to save time
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            j, k = i + 1, len(nums) - 1
            
            while j < k:
                current_sum = nums[i] + nums[j] + nums[k]
                
                if current_sum == target:
                    return current_sum  # Perfect match
                
                # Update closest_sum if the current one is nearer to target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum
                
                # Move pointers based on comparison with target
                if current_sum < target:
                    j += 1
                else:
                    k -= 1
                    
        return closest_sum