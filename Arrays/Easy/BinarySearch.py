class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        L, R = 0, len(nums)-1

        while L<=R:
            mid = (R+L)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                R=mid-1
            elif nums[mid]<target:
                L=mid+1
        return -1