class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        memo = {}

        def dfs(a, b):

            if (a, b) in memo:
                return memo[(a, b)]

            # identical strings
            if a == b:
                return True

            # different character counts
            if sorted(a) != sorted(b):
                return False

            n = len(a)

            for i in range(1, n):

                # without swap
                if (dfs(a[:i], b[:i]) and
                    dfs(a[i:], b[i:])):

                    memo[(a, b)] = True
                    return True

                # with swap
                if (dfs(a[:i], b[n - i:]) and
                    dfs(a[i:], b[:n - i])):

                    memo[(a, b)] = True
                    return True

            memo[(a, b)] = False
            return False

        return dfs(s1, s2)