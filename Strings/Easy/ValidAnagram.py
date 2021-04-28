class Solution:
    #Time O(N), Space O(N)
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for c in s:
            letters[c]=letters.get(c,0)+1
        
        for c in t:
            if c in letters:
                letters[c]-=1
                if letters[c]==0:
                    del letters[c]
            else:
                return False
        return len(letters)==0
    
    # Basic. Time O(depends on sort as well), Space O(depends on how much space the sort takes up)
    # Both are probably around O(N logN) 
    # def isAnagram(self, s: str, t: str) -> bool:
    #     s = "".join(sorted(s))
    #     t = "".join(sorted(t))
    #     # print(s,t)
    #     return s==t