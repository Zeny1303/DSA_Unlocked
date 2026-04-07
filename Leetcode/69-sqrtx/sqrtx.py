class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        
        left, right = 1, x // 2  # sqrt(x) is always ≤ x//2 for x >= 4
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right  # right is the floor when loop ends

