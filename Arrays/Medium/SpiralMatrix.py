class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        resList = []
        top=0
        bottom=len(matrix)
        left=0
        right=len(matrix[0])
        
        while left<right and top<bottom:

            #right
            for i in range(left,right):
                resList.append(matrix[top][i])#row,col
            top+=1#narrow down the available for iteration space in the matrix    
                
            #down
            for i in range(top,bottom):
                resList.append(matrix[i][right-1])
            right-=1
            
            if not (left<right and top<bottom):
                break
            #left
            for i in range(right-1, left-1,-1):
                resList.append(matrix[bottom-1][i])
            bottom-=1
            #up
            for i in range(bottom-1,top-1,-1):
                resList.append(matrix[i][left])
            left+=1
            
        return resList