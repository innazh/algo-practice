#Plan:
#Figure out how to get a single digit
    #count the num of digits in num
    #convert the idx of figit we're looking for to the proper power of 10
#Take care of edge cases: empty input or just has 1 digit
#Put together a for loop
#Figure out how to store data (a list of strings)
#Convert the data back to the format required by the task (int)


def getDigit(num, i, totalDigits):
    idx = totalDigits-i+1 #gotta reverse i: the closer the num we're looking to extaract is to the first digit, the greater the power multiplier of 10 needs to be
    val = num/pow(10,idx)
    # print(val)
    if int(val)>0:
        valNoRemainant = num//pow(10,idx)
        # print(valNoRemainant)
        res = val%valNoRemainant
        # print(res)
        res = round(res,5)
    else:
        res = val
    # print("result="+str(int(res*10)))
    return int(res*10)

def countDigits(nums):
    count=0
    if nums==0:
        return 1

    while int(nums)>0:
        nums/=10
        count+=1 
    return count

#Not theeasiest question tbh....
def reversePairs(nums) -> int:
    if not nums:
        return nums
    total = countDigits(nums)
    if total<=1:
        return nums

    res = []
    j=2
    for i in range(1,total+1,2):
        first = getDigit(nums, i, total)
        if j<=total:
            second = getDigit(nums, j, total)
            res.append(str(second))
        res.append(str(first))
        j+=2

    return int("".join(res))

def main():
    print(reversePairs(12345)) #returns 21435
    print(reversePairs(345098)) #430589
    print(reversePairs(0)) #0
    print(reversePairs(2)) #2
    print(reversePairs(34)) #43
    print(reversePairs(None)) #43
    print(reversePairs(100)) #43

    print(reversen(4562))

if __name__=="__main__":
    main()

def plainReverse(n):
    rev = 0
    
    while(n > 0):
        a = n % 10
        print("a="+str(a))
        rev = rev * 10 + a
        print("rev="+str(rev))
        n = n // 10
        print("n="+str(n))
    return rev