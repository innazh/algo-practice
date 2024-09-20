# solved it myself, I definetly have no problem understanding the concepts but the math-y formul-y things like calculating a particular index based on some number is such a drag.
# tbh pretty proud cause this is very different from a solution video that I watched afterwards.
# Here I'm visualizing the matrix as a continuous array, then calculating the indexes.
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        L,  R = 0, len(matrix)*len(matrix[0]) - 1
        
        while L<=R:
            # get the middle
            mid = (L+R)//2
            mid_value = None
            row = mid // len(matrix[0])
            col = mid % len(matrix[0])
            mid_value = matrix[row][col]
            # BS
            if mid_value==target:
                return True
            elif mid_value<target:
                L = mid + 1                
            elif mid_value>target:
                R = mid - 1
        return False