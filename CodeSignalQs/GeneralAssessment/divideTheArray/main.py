#not done
def divideArray(a):
    j=len(a)-1
    a1 = []
    a2 = []
    d1 = {}
    
    d2 = {}
    while 
        if not a[i] in d1.values():
            d1[a[i]] = i #or 1
            a1.append(a[i])
        if not a[j] in d2.values():
            a2.append(a[j])
            d2[a[j]] = j
        j-=1
        
    return [a1,a2]

def main():
    a1 = [2,1,2,3,3,4] #[[1,2,3],[2,3,4]] OR [[4,2,3],[3,2,1]]
    a2 = [2,2,3,3,2,2] #[], - impossible. If two arrays are of equal length then at least one of them gonna contain two 2s
    
if __name__=="__main__":
    main()