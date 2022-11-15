class Solution(object):
    #time is O(n)-worst case, space is O(n)
    def twoSum(arr, sum):
        res = []
        d = {}

        for idx, x in enumerate(arr):
            remainder = sum - x
            y = d.get(remainder, -1) #alt: if remainder in d
            if y!=-1:
                res.append(remainder)
                res.append(x)
                break
            else:
                d[x] = idx

        return res

    #classic sort + list | space: worst is O(n), best O(1), time: O(nlogn), timsort
    def twoSumSort(arr, sum):
        res = []
        high = len(arr)-1
        low = 0
        temp_sum = 0

        arr.sort() #space: worst is O(n), best O(1), time: O(nlogn), timsort.
        while temp_sum!=sum:
            temp_sum = arr[low] + arr[high]
            if  temp_sum > sum:
                high-=1
                if high<0:
                    high = len(arr)-1
            elif temp_sum < sum:
                low+=1
                if low==len(arr):
                    low = 0
            elif temp_sum == sum:
                res.append(arr[low])
                res.append(arr[high])

        return res

print(Solution.twoSum([2,7,11,15], 18))
