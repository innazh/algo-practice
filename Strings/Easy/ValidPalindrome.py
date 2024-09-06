class Solution:
    #O(1) space, O(n) time solution
    def isPalindrome(self, s: str) -> bool:
        start = 0 
        end = len(s) - 1 
        result = True
        
        while start<=end:
            while start<=end:
                if s[start].isalpha() or s[start].isdigit():
                    break
                start+=1
            
            while start<=end:
                if s[end].isalpha() or s[end].isdigit():
                    break
                end-=1
            
            if start>=end:
                break
                
            if s[start].lower()!=s[end].lower():
                result=False
                break

            start+=1
            end-=1
                
        return result


    #O(n) - space, O(n) - time
    def isPalindrome(self, s: str) -> bool:
        potentialPalindrome = []
        
        for i in range(0,len(s)):
            if s[i].isalpha() or s[i].isdigit():
                potentialPalindrome.append(s[i].lower())
        
        #check if it is
        end=len(potentialPalindrome)-1
        for start in range(0,len(potentialPalindrome)):
            if potentialPalindrome[end]!=potentialPalindrome[start]:
                return False
            end-=1
        return True
    
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p1 = 0
        p2 = len(s)-1
        while p1<p2:
            while not s[p1].isalpha() and not s[p1].isnumeric() and p1 < p2:
                p1+=1
            while not s[p2].isalpha() and not s[p2].isnumeric() and p1 < p2:
                p2-=1
            print(p1,p2)
            if p1<p2:
                print("hit",p1,p2)
                if s[p1].lower()!=s[p2].lower():
                    return False
            p1+=1
            p2-=1

        return True