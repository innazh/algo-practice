#Note: read about bit manipulation and practice it, seems like no space linear solution is the bit manipulation one
#Now trying for the second linear solution with no extra space.
#Results: no explicit extra space is used, however python's sort function still uses some extra space and time under the hood
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        res=-1
        nums.sort()
        found=False
        i=0
        
        while i<len(nums)-1 and not found:
            if nums[i]!=nums[i+1]:
                    res = nums[i]
                    found=True
            if not found:
                n = nums[i]
                while n==nums[i]:
                    i+=1
        if not found:
            res = nums[len(nums)-1]
            
        return res

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