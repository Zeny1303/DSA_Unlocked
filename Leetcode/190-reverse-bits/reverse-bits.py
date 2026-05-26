class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """

        result = 0

        for i in range(32):

            # Shift result left
            result <<= 1

            # Add last bit of n
            result |= (n & 1)

            # Shift n right
            n >>= 1

        return result