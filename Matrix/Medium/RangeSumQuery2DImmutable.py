# This was my first attempt at the problem. Although this is not EXACTLY O(1), this makes me really proud 'cause I reasoned through it myself
# without any hints, help or lookups. What makes it even better (in my opinion), is that it's definetely not the "right"/ideal solution which
# other people typically come up with and use in the explanation videos. I understood & solved it my own way. 
# I'll still go through the more 'optimal' solution in a bit.
class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix=matrix
        
        self.rows = len(matrix)
        self.cols = len(matrix[0])

        self.pre_computed_rows = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        for r in range(self.rows):
            rowSum=0
            for c in range(self.cols):
                rowSum+=matrix[r][c]
                self.pre_computed_rows[r][c]=rowSum        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        squareSum = 0
        for row in range(row1,row2+1):
            leftSum = self.pre_computed_rows[row][col1-1] if col1-1>=0 else 0
            square_row_sum = self.pre_computed_rows[row][col2] - leftSum
            squareSum = squareSum + square_row_sum
        return squareSum

        
# Better solution, mosto optimal. Same concept but presum is a matrix, we're summing up the nums to the left and above.
# We create a padding of zeroes as an extra row and col to make sure we're not going outta bounds and havinga lots of if statements.

class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix=matrix
        
        rows = len(matrix)
        cols = len(matrix[0])

        self.sumMat = [[0] * (cols + 1) for r in range(rows+1)]
        for r in range(rows):
            rowSum = 0
            for c in range(cols):
                rowSum += matrix[r][c]
                above = self.sumMat[r][c+1]
                self.sumMat[r+1][c+1] = rowSum + above        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        row1, row2, col1, col2 = row1+1, row2+1, col1+1, col2+1
        left = self.sumMat[row2][col1-1]
        above = self.sumMat[row1-1][col2]
        topLeft = self.sumMat[row1-1][col1-1]
        bottomRight = self.sumMat[row2][col2] - above - left + topLeft
        return bottomRight