def mutateTheArray(n, a):
    b = [None]*n
    for i in range(n):
        a1=0
        a2=0
        if i-1>=0:
            a1 = a[i-1]
        if i+1<n:
            a2 = a[i+1]

        b[i] = a1+a2+a[i]

    return b

def main():
    print(mutateTheArray(5, [4, 0, 1, -2, 3]))
    print("ab1c" > "1zz456")

if __name__=="__main__":
    main()