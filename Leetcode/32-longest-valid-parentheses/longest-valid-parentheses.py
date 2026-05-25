class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = [-1]
        max_length = 0

        for i in range(len(s)):

            # Opening bracket
            if s[i] == '(':
                stack.append(i)

            else:

                # Pop matching '('
                stack.pop()

                # Stack became empty
                if not stack:
                    stack.append(i)

                else:
                    max_length = max(
                        max_length,
                        i - stack[-1]
                    )

        return max_length