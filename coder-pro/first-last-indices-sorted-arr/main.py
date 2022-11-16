class Solution(object):
    #O(1) space, O(logn) time  
    def getRange(self, arr, target):
        # calling both of these with the same range because we don't know where the firs and last nums are
        first = self.binarySearch(arr, 0, len(arr)-1, target, True)
        last = self.binarySearch(arr, 0, len(arr)-1, target, False)
        return [first, last]

    # find first is the boolean to find first index of the target number
    def binarySearch(self, arr, low, high, target, findFirst):
        while True:
            mid = (high + low) // 2 #low + (high - low) // 2#
            if findFirst:
                if mid == 0 or arr[mid-1] < target and arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if mid==len(arr)-1 or arr[mid+1] > target and arr[mid] == target:
                    return mid
                elif arr[mid] > target:
                    high = mid - 1
                else: 
                    low = mid + 1


print(Solution().getRange([1, 3, 3, 5, 7, 8, 9, 9, 9, 15], 9))
print(Solution().getRange([9,9,9,9,9,9,9], 9))
