class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        def is_palindrome(word):
            return word == word[::-1]

        word_map = {}

        for i, word in enumerate(words):
            word_map[word] = i

        result = []

        for i, word in enumerate(words):

            for j in range(len(word) + 1):

                prefix = word[:j]
                suffix = word[j:]

                # Case 1:
                # Prefix is palindrome
                if is_palindrome(prefix):

                    rev_suffix = suffix[::-1]

                    if (rev_suffix in word_map and
                        word_map[rev_suffix] != i):

                        result.append([word_map[rev_suffix], i])

                # Case 2:
                # Suffix is palindrome
                # j != len(word) avoids duplicates
                if j != len(word) and is_palindrome(suffix):

                    rev_prefix = prefix[::-1]

                    if (rev_prefix in word_map and
                        word_map[rev_prefix] != i):

                        result.append([i, word_map[rev_prefix]])

        return result