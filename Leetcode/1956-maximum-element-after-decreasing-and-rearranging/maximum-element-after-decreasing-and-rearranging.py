class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Step 1: Sort the array to process elements in increasing order
        arr.sort()
        
        # Step 2: The first element must always be reduced to 1
        current_max = 1
        
        # Step 3: Iterate through the rest of the elements
        for i in range(1, len(arr)):
            # The next element can at most be current_max + 1
            # But it cannot exceed its own original value (we can only decrease it)
            if arr[i] > current_max:
                current_max += 1
                
        return current_max