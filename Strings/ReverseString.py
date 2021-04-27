# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

class Solution:
    def dealWithNegative(self,x) -> int:
        d=1
        if x<0:
            d=-1
        return d
    
    def reverse(self, x: int) -> int:
        if x==0:
            return x
        
        d = self.dealWithNegative(x)
        x=x*d
        
        rev=[]
        while x!=0:
            digit = x%10
            x//=10
            rev.append(str(digit))
            # rev = rev * 10 + digit
        res = int("".join(rev))
        if res > pow(2, 31) - 1 or res < -pow(2, 31):
            return 0
        return res*d
            