class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols

        max_area = 0

        for row in matrix:

            # build histogram
            for i in range(cols):

                if row[i] == "1":
                    heights[i] += 1
                else:
                    heights[i] = 0

            # largest rectangle in histogram
            stack = []

            for i in range(cols):

                start = i

                while stack and stack[-1][1] > heights[i]:

                    index, height = stack.pop()

                    max_area = max(
                        max_area,
                        height * (i - index)
                    )

                    start = index

                stack.append((start, heights[i]))

            # remaining stack
            for index, height in stack:

                max_area = max(
                    max_area,
                    height * (cols - index)
                )

        return max_area