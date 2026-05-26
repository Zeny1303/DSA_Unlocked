class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        n = len(words)

        masks = [0] * n

        lengths = [len(word) for word in words]

        # Create bitmask for each word
        for i, word in enumerate(words):

            mask = 0

            for ch in word:

                mask |= 1 << (ord(ch) - ord('a'))

            masks[i] = mask

        answer = 0

        # Compare all pairs
        for i in range(n):

            for j in range(i + 1, n):

                # No common letters
                if masks[i] & masks[j] == 0:

                    answer = max(answer, lengths[i] * lengths[j])

        return answer