#initial bruteforce-based solution using a dictionary to keep track on how many times each element is present, 
#then iterating through the dictionary to find the element that is only encountered once
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        encountered = {}
        res=-1
        
        for i in range(len(nums)):
            if nums[i] in encountered.keys():
                encountered[nums[i]] = encountered[nums[i]] + 1
            else:
                encountered[nums[i]] = 1
        
        for j in encountered:
            if encountered[j]==1:
                res=j
                break
                
        return j