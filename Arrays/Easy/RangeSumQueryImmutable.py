#prefix, init is O(n) but sumrange is roughly O(1)
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefix_sum = []
        curr_sum=0
        for num in nums:
            curr_sum+=num
            self.prefix_sum.append(curr_sum)
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        left_side = 0
        if left-1>=0:
            left_side = self.prefix_sum[left-1]
        result = self.prefix_sum[right]-left_side
        return result