class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        # Edge case
        if num1 == "0" or num2 == "0":
            return "0"

        m = len(num1)
        n = len(num2)

        # Result can have at most m+n digits
        result = [0] * (m + n)

        # Multiply from right to left
        for i in range(m - 1, -1, -1):

            for j in range(n - 1, -1, -1):

                mul = int(num1[i]) * int(num2[j])

                # Positions
                p1 = i + j
                p2 = i + j + 1

                # Add current multiplication
                total = mul + result[p2]

                result[p2] = total % 10
                result[p1] += total // 10

        # Convert to string
        answer = ""

        for digit in result:

            # Skip leading zeros
            if not (len(answer) == 0 and digit == 0):
                answer += str(digit)

        return answer