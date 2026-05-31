class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False

        divisor_sum = 1

        i = 2
        while i * i <= num:
            if num % i == 0:
                divisor_sum += i

                if i != num // i:
                    divisor_sum += num // i

            i += 1

        return divisor_sum == num