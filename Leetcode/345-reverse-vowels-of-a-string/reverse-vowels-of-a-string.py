class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        vowels = set('aeiouAEIOU')

        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:

            # Move left pointer
            while left < right and s[left] not in vowels:
                left += 1

            # Move right pointer
            while left < right and s[right] not in vowels:
                right -= 1

            # Swap vowels
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        return ''.join(s)