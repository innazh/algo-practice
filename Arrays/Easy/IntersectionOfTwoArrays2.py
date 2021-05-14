class Solution:
    #Space O(n) - depends on nums1, Time O(n) - depends on nums2 => O(num1+nums2)
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        numbers = {}
        for num in nums1:
            numbers[num] = numbers.get(num, 0) + 1
        for d in nums2:
            if d in numbers and numbers.get(d)>0:
                result.append(d)
                numbers[d]-=1
        return result

# class Solution:
#     #O(nlogn) time, O(n) space(if we take sort into account)
#     def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         result = []
#         nums1.sort() #O(nlogn)
#         nums2.sort() #O(nlogn)
#         i=0
#         j=0
#         while i<len(nums1) and j<len(nums2): #O(n)
#             if nums1[i]==nums2[j]:
#                 result.append(nums1[i])
#                 i+=1
#                 j+=1
#             elif nums1[i]>nums2[j]:
#                 j+=1
#             else:
#                 i+=1
#         return result

# Follow up:

# What if the given array is already sorted? How would you optimize your algorithm?
    # If so, then I wouldn't need to sort and my algorithm would have O(n) complexity
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
    #
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
