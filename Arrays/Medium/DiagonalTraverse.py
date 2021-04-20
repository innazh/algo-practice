class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        num_rows, num_cols = len(matrix), len(matrix[0])
        diagonals = [[] for _ in range(num_rows + num_cols - 1)]
        
        for i in range(num_rows):
            for j in range(num_cols):
                diagonals[i + j].append(matrix[i][j])
        
        res = diagonals[0]
        
        for x in range(1, len(diagonals)):
            if x % 2 == 1:
                res.extend(diagonals[x])
            else:
                res.extend(diagonals[x][::-1])
        
        return res
