class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        '''
        jab hum 3th
        '''
        result =[]
        for i in range(numRows):
            result.append([1 for _ in range(i+1)])
            for j in range(1,i):
                result[i][j] = result[i-1][j] + result[i-1][j-1]
        return result        

        