# This solution takes into account edge case with len 0 array even tho LC is not testing for it 
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return 1

        L = 0
        R = L + 1
        while L<len(nums) and R<len(nums):
            while R<len(nums) and nums[R]==nums[L]:
                R+=1
            if R<len(nums):
                nums[L+1]=nums[R]
            L+=1
        return L
# Simplified solution:
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = 1
        for R in range(1, len(nums)):
            if nums[R]!=nums[R-1]:
                nums[L]=nums[R]
                L+=1
        return L