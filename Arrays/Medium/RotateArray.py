class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %=n #account for situations when k>len(nums)
        
        start = count = 0
        
        while count < n:
            current=start
            prev = nums[start]
            while True:
                next_idx = (current + k) % n #in case this goes out of bounds
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count+=1

                if start == current:
                    break
            start+=1
        
        
#         k = k % len(nums)
#         self.reverse(nums,0,len(nums)-1)
#         self.reverse(nums,0,k-1)
#         self.reverse(nums,k,len(nums)-1)
    
#     def reverse(self, nums, start, end):
#         while end>start:
#             temp = nums[start]
#             nums[start]=nums[end]
#             nums[end]=temp
#             end-=1
#             start+=1