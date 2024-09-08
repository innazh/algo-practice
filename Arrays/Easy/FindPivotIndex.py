class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        totalSum = sum(nums) #O(n)
        leftSum=0
        for i in range(len(nums)):
            rightSum = totalSum - nums[i] - leftSum
            if rightSum==leftSum:
                return i
            leftSum += nums[i]
        return -1
        