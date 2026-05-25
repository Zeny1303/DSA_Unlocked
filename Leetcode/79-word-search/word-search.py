class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, index):

            # word completely found
            if index == len(word):
                return True

            # out of bounds or mismatch
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                board[r][c] != word[index]):
                return False

            temp = board[r][c]
            board[r][c] = "#"

            # explore 4 directions
            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )

            # backtrack
            board[r][c] = temp

            return found

        for r in range(rows):
            for c in range(cols):

                if dfs(r, c, 0):
                    return True

        return False