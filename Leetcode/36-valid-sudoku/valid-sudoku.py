class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                value = board[r][c]

                # Ignore empty cells
                if value == '.':
                    continue

                # Box index
                box_index = (r // 3) * 3 + (c // 3)

                # Check duplicates
                if (
                    value in rows[r] or
                    value in cols[c] or
                    value in boxes[box_index]
                ):
                    return False

                rows[r].add(value)
                cols[c].add(value)
                boxes[box_index].add(value)

        return True