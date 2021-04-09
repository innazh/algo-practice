# In a given integer array nums, there is always exactly one largest element.

# Find whether the largest element in the array is at least twice as much as every other number in the array.

# If it is, return the index of the largest element, otherwise return -1.

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxNum=0
        maxNumIdx=-1
        secondMax=0
        for i in range(0,len(nums)):
            if maxNum<nums[i]:
                secondMax=maxNum
                maxNum=nums[i]
                maxNumIdx=i
            if secondMax<nums[i] and nums[i]!=maxNum:
                secondMax=nums[i]
        print(secondMax)
        print(maxNum)
        if secondMax==0:
            return maxNumIdx
        elif maxNum/secondMax>=2:
            return maxNumIdx
        else:
            return -1

#https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/