# Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i]==9:
                digits[i]=0
                if i==0: #if we are in the beginning of the list
                    digits.insert(i,1)
            else:
                digits[i]=digits[i]+1
                break
        return digits
                
#https://leetcode.com/problems/plus-one/