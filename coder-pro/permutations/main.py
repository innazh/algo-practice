class Solution(object):
    def _permuteHelper(self, nums, start=0):
        if start==len(nums):
            return [nums.copy()]
        result = []
        for i in range(start, len(nums)):
            nums[start],nums[i] = nums[i], nums[start]
            result += self._permuteHelper(nums, start+1)
            nums[start],nums[i] = nums[i], nums[start]

        return result


    def permute(self, nums):
        return self._permuteHelper(nums)

    def permutev2(self, nums, values=[]):
        if not nums:
            return [values] #of no numbers are passed in (whole array is excluded from being premuted) return the constructed array
        result = []
        for i in range(len(nums)):
            result += self.permutev2(nums[:i] + nums[i+1:], values + [nums[i]])
        return result
        


print(Solution().permute([1,2,3]))
print(Solution().permutev2([1,2,3]))

# print(Solution().permute([1,2,3,4]))




# O(n!)
# [1,2,3,4]
# 4*(3*2*1)
# total combinations: 24
# [1,2,3,4]
# [1,2,4,3]
# [1,3,2,4]
# [1,3,4,2]
# [1,4,3,2]
# [1,4,2,3]