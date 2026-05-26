from collections import defaultdict, deque

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :rtype: List[List[str]]
        """

        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        # Graph + distance
        parents = defaultdict(list)
        level = {beginWord}
        visited = set()

        found = False

        # BFS to build shortest path graph
        while level and not found:

            next_level = defaultdict(list)

            for word in level:
                visited.add(word)

            for word in level:

                for i in range(len(word)):

                    for c in 'abcdefghijklmnopqrstuvwxyz':

                        new_word = word[:i] + c + word[i+1:]

                        if new_word in wordSet and new_word not in visited:

                            next_level[new_word].append(word)

                            if new_word == endWord:
                                found = True

            level = next_level

            for word in next_level:
                parents[word].extend(next_level[word])

        result = []

        # Backtracking to build paths
        def backtrack(word, path):

            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                backtrack(parent, path + [parent])

        if found:
            backtrack(endWord, [endWord])

        return result