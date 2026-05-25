class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        numbers = []
        fact = 1

        # create numbers list and factorial
        for i in range(1, n):
            fact *= i

        for i in range(1, n + 1):
            numbers.append(str(i))

        k -= 1   # convert to 0-indexing

        result = ""

        while True:

            index = k // fact
            result += numbers[index]

            numbers.pop(index)

            if not numbers:
                break

            k = k % fact
            fact = fact // len(numbers)

        return result