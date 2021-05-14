from test_vals import *
import math
import time
import heapq

# def sortedInsert(arr, num):
#     inserted=False
#     for i in range(len(arr)):
#         if arr[i]>=num:
#             arr.insert(i, num)
#             inserted=True
#             break
#     if not inserted:
#         arr.append(num)
#     return    

def performOperation(num):
    res = math.floor(num/2)
    return res

def minSum(num, k):
    size = len(num)    
    if size==0:
        return 0
    heap = [n*-1 for n in num] 
    heapq.heapify(heap)

    operations=0
    
    while operations<k:
        n = performOperation(heapq.heappop(heap))
        operations+=1
        heapq.heappush(heap,n)
    return sum(heap)*-1

# def minSum(num, k):
#     size = len(num)    
#     if size==0:
#         return 0
    
#     num.sort()
#     i = size-1
#     operations=0
    
#     while operations<k:
#         n = performOperation(num.pop(i))
#         operations+=1
        
#         sortedInsert(num, n)    
#     return sum(num)

def main():
    # print(minSum(test3_l, test3_k))
    # print(minSum2([10000]*3,3))
    # minSum2([1000,30,50,100,50000], 5)
    start = time.time()
    print(minSum2(test8_l, test8_k))
    end = time.time()
    print("Time consumed in working: ",end - start) #55.89

    start = time.time()
    print(minSum([10000]*10000, test5_k)) #5
    end = time.time()
    print("Time consumed in working: ",end - start) #0.4


    #TEST!!!!!!

    # start = time.time()
    # print(minSum([10000]*3000, test5_k)) #5
    # end = time.time()
    # print("Time consumed in working: ",end - start) #0.4

    # start = time.time()
    # print(minSum([10000]*6000, test5_k)) #5
    # end = time.time()
    # print("Time consumed in working: ",end - start) #0.4

    # start = time.time()
    # print(minSum([10000]*12000, test5_k)) #5
    # end = time.time()
    # print("Time consumed in working: ",end - start) #0.4




if __name__ == '__main__':
    main()