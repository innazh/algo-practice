class Solution:
    #working on O(1) space, O(n) time solution
    def isPalindrome(self, s: str) -> bool:
        start = 0 
        end = len(s) - 1 
        result = True
        
        while start<=end:
            while not s[start].isalpha() or not s[start].isdigit():
                start+=1
                if start>=end:
                    break

            while not s[end].isalpha() or not s[end].isdigit():
                end-=1
                if end<=start:
                    break
                    
            if s[start].lower()!=s[end].lower():
                result=False
                break
            else:
                start+=1
                end-=1
            if start==end:
                break
                
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