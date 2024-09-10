class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow==fast:
                break
        
        slow2=0
        while slow2!=slow:
            slow2=nums[slow2]
            slow=nums[slow]
        return slow
    #O(1) space & O(n) time
    # Floyd's algorithm, it's a LL cycle problem.