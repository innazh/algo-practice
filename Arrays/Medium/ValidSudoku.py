class Solution:
    def validSubBox(self, box):
        nums = set()
        for i in range(len(box)):
            for j in range(len(box[0])):
                if box[i][j] in nums:
                    return False
                if box[i][j]!='.':
                    nums.add(box[i][j])
        return True                
    
    #Linear time&space, depends on the number of filled cells
    def validLine(self, line):
        valid=True
        nums = {}
        for num in line:
            if num in nums:
                valid=False
                break
            if num!='.':
                nums[num]=nums.get(num, 0)+1
        return valid
        
    def validCol(self, board):
        for col in zip(*board):
            if not self.validLine(col):
                return False
        return True
    
    def validRow(self,board):
        for row in board:
            if not self.validLine(row):
                return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        result=True
        miniboard=[]
        for boxCol in (0,3,6):
            for boxRow in range(0,9):
                row = board[boxRow]
                miniboard.append(row[boxCol:boxCol+3])
                if (boxRow+1)%3==0:
                    if not self.validSubBox(miniboard):
                        result = False
                        break
                    miniboard=[]
        
        return result and self.validCol(board) and self.validRow(board)