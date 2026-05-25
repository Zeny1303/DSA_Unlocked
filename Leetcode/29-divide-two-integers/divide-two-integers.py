class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign
        negative = (
            (dividend < 0 and divisor > 0) or
            (dividend > 0 and divisor < 0)
        )

        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0

        while dividend >= divisor:

            temp = divisor
            multiple = 1

            # Double divisor until it exceeds dividend
            while dividend >= (temp << 1):

                temp <<= 1
                multiple <<= 1

            dividend -= temp
            result += multiple

        return -result if negative else result