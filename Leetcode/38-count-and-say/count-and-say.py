class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        result = "1"

        for _ in range(n - 1):

            current = ""
            count = 1

            for i in range(1, len(result)):

                # Same digit
                if result[i] == result[i - 1]:
                    count += 1

                else:
                    current += str(count)
                    current += result[i - 1]
                    count = 1

            # Last group
            current += str(count)
            current += result[-1]

            result = current

        return result