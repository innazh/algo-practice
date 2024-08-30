class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_so_far = {}
        for idx, num in enumerate(nums):
            seeking_num = target - num
            if seeking_num in nums_so_far:
                return nums_so_far[seeking_num],idx
            nums_so_far[num] = idx
        return
        