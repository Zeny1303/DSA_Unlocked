class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]

        for i in range(n):
            # Reflect current list and add leading bit
            for num in reversed(result):
                result.append(num | (1 << i))

        return result