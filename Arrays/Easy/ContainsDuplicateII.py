class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = {}
        for i,num in enumerate(nums):
            if num in hashmap:
                if abs(hashmap[num]-i)<=k:
                    return True
                else:
                    del hashmap[num]
            hashmap[num]=i
        return False
        