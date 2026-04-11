class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        firstRowImpacted = False
        firstColImpacted = False
        # is firstrowimpacted and secondrow impacted or not ?
        for col in range(n):
            if matrix[0][col] == 0:
                firstRowImpacted = True
                break
        for row in range(m):
            if matrix[row][0] == 0:
                firstColImpacted = True
                break   

        # set the guards means first element of col or row should be mark as impacted mean 0
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == 0:
                    matrix[i][0] =0 
                    matrix[0][j] =0


        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][0] == 0 or matrix[0][j] ==0:
                    matrix[i][j] =0 
                    
        if firstRowImpacted:
            for j in range(n):
                matrix[0][j] = 0
        if firstColImpacted:
            for i in range(m):
                matrix[i][0] = 0                    