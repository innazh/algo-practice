class Solution:
    #Time O(N), Space O(N)
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}
        result=False
        
        for i in range(len(nums)):
            if nums[i] in hashmap:
                result=True
            else:
                hashmap[nums[i]]=i
                
        return result
    
    
    #Time O(n^2) would be the double for loop solution (aka bubble sort style)
    #Time O(NlogN), Space(1)
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         result = False
#         nums.sort();
        
#         for i in range(1,len(nums)):
#             if nums[i]==nums[i-1]:
#                 result=True
#                 break
#         return result