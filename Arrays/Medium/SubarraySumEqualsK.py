class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        res=0
        currSum = 0
        prefixSums = {0:1} #how many times sums are occurring within the array
        # as we're going through the array, we're recording the on-going running sum and all the prefix sums that we've encountered thus far.
        # this allows us to see if we've encountered a prefix sum before, subtracting which from the current running sum, will result in the subarray
        # that sums up to k

        # this lowkey reminds me of two sum
        # storing ecountered vals in a hashmap and looking back, checking if there's the diff we're looking for, while iterating forward
        for num in nums:
            currSum += num
            diff = currSum - k

            res += prefixSums.get(diff, 0)
            prefixSums[currSum] = 1 + prefixSums.get(currSum, 0)
        return res
    