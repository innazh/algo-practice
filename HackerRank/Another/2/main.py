from tests import *

def isDivisible(s, t):
    res = False
    if len(s)%len(t)!=0:
        return res
    
    divisor = t
    print("divisor="+divisor)
    while divisor!=s and len(divisor)<len(s):
        divisor+=t
    if divisor==s:
        res=True
    return res

def findSmallestDivisor(s, t):
    length = -1

    if isDivisible(s,t):
        for i in range(1,len(t)+1):
            substr=t[:i]
            if isDivisible(t, substr):
                length = len(substr)
                break
    return length

def main():
    print(findSmallestDivisor(s5,t5))
    print(findSmallestDivisor(s8,t8))
    print(findSmallestDivisor(s9,t9))


if __name__ == '__main__':
    main()