class Solution:
    #Time O(N), Space O(N)
    def firstUniqChar(self, s: str) -> int:
        unique = {}
        for i in range(len(s)):
            #in the dict we wanna put a list where first item is idx and second item is occurrence count
            lst = unique.get(s[i], []) #see if item exists
            if len(lst)<2:
                unique[s[i]] = [i, 1]
            else:
                unique[s[i]] = [lst[0], lst[1]+1]
        # print(unique)
        for i in unique:
            if unique[i][1]==1:
                return unique[i][0]

        return -1


#Brute FOrce O(N^2) Time, O(1) Space
    # def firstUniqChar(self, s: str) -> int:
    #     for i in range(len(s)):
    #         char = s[i]
    #         unique = True
    #         for j in range(len(s)):
    #             if(j!=i):
    #                 if char==s[j]:
    #                     unique=False
    #                     break
    #         if unique:
    #             return i
    #     return -1