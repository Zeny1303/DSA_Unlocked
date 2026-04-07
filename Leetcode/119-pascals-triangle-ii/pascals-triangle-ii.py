class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1] * (rowIndex + 1)      # start with all 1s

        for i in range(2, rowIndex + 1):         # row number
            for j in range(i - 1, 0, -1):        # right to left, skip edges
                row[j] = row[j] + row[j - 1]

        return row