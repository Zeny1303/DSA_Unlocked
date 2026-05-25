class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        if len(s) <= 1:
            return s

        start = 0
        end = 0

        # Function to expand from center
        def expand(left, right):

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # length of palindrome
            return right - left - 1

        for i in range(len(s)):

            # Odd length palindrome
            len1 = expand(i, i)

            # Even length palindrome
            len2 = expand(i, i + 1)

            max_len = max(len1, len2)

            # Update answer
            if max_len > (end - start):

                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]