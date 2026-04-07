class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]                    # base row

        for i in range(1, numRows):
            prev = triangle[i - 1]
            row  = [1]                      # left edge

            for j in range(1, i):           # interior elements
                row.append(prev[j-1] + prev[j])

            row.append(1)                   # right edge
            triangle.append(row)

        return triangle