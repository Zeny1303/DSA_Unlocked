class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)

        # palindrome[i][j] = True if s[i:j+1] is palindrome
        palindrome = [[False] * n for _ in range(n)]

        cuts = [0] * n

        for end in range(n):

            min_cut = end

            for start in range(end + 1):

                # Check palindrome
                if (s[start] == s[end] and
                    (end - start <= 2 or palindrome[start + 1][end - 1])):

                    palindrome[start][end] = True

                    # No cut needed
                    if start == 0:
                        min_cut = 0
                    else:
                        min_cut = min(min_cut, cuts[start - 1] + 1)

            cuts[end] = min_cut

        return cuts[n - 1]