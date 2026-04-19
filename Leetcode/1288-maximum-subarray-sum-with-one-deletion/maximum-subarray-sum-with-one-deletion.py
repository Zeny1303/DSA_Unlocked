class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # choice -> delete = 0 mtb nodelete or delete = 1 mtb 1 delete hua hai 
        oneDelete=float("-inf")
        noDelete = arr[0]
        res = arr[0]
        for i in range(1, len(arr)):
            # Standard Kadane's: Max sum ending at i with NO deletions
            current_no_delete = max(arr[i], noDelete + arr[i])
            
            # Max sum ending at i with ONE deletion
            # Either we used the deletion earlier (oneDelete + arr[i])
            # Or we delete arr[i] right now (noDelete)
            oneDelete = max(oneDelete + arr[i], noDelete)
            
            # Update noDelete for the next iteration
            noDelete = current_no_delete
            
            # The answer is the best we've seen from either state
            res = max(res, noDelete, oneDelete)
        return res    