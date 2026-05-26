class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """

        last_index = {}

        # Store last occurrence of each character
        for i, ch in enumerate(s):
            last_index[ch] = i

        stack = []

        seen = set()

        for i, ch in enumerate(s):

            # Skip duplicates
            if ch in seen:
                continue

            # Maintain lexicographically smallest order
            while (stack and
                   ch < stack[-1] and
                   last_index[stack[-1]] > i):

                removed = stack.pop()

                seen.remove(removed)

            stack.append(ch)

            seen.add(ch)

        return "".join(stack)