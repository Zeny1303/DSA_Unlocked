class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        stack = []
        max_area = 0

        for i in range(len(heights)):

            start = i

            while stack and stack[-1][1] > heights[i]:

                index, height = stack.pop()

                max_area = max(
                    max_area,
                    height * (i - index)
                )

                start = index

            stack.append((start, heights[i]))

        # remaining bars
        for index, height in stack:

            max_area = max(
                max_area,
                height * (len(heights) - index)
            )

        return max_area