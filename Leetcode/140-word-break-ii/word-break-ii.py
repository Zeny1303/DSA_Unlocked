class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        wordSet = set(wordDict)

        memo = {}

        def dfs(start):

            # Already computed
            if start in memo:
                return memo[start]

            # Reached end
            if start == len(s):
                return [""]

            result = []

            for end in range(start + 1, len(s) + 1):

                word = s[start:end]

                if word in wordSet:

                    remaining_sentences = dfs(end)

                    for sentence in remaining_sentences:

                        if sentence:
                            result.append(word + " " + sentence)
                        else:
                            result.append(word)

            memo[start] = result

            return result

        return dfs(0)