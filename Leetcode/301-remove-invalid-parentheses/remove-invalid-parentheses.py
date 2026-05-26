from collections import deque

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def is_valid(string):

            count = 0

            for ch in string:

                if ch == '(':
                    count += 1

                elif ch == ')':

                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        result = []

        queue = deque([s])

        visited = set([s])

        found = False

        while queue:

            curr = queue.popleft()

            # Valid expression found
            if is_valid(curr):

                result.append(curr)
                found = True

            # Stop generating deeper levels
            if found:
                continue

            for i in range(len(curr)):

                # Remove only parentheses
                if curr[i] not in '()':
                    continue

                next_str = curr[:i] + curr[i+1:]

                if next_str not in visited:

                    visited.add(next_str)
                    queue.append(next_str)

        return result