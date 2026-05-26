class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        first = float('inf')
        second = float('inf')

        for num in nums:

            # Smallest number so far
            if num <= first:
                first = num

            # Second smallest
            elif num <= second:
                second = num

            # Found third larger number
            else:
                return True

        return False