#Get prime number's index. Prime numbers from 2 to 100.
def getPrimeNumber(idx):
    result = -1
    primeNums = []
    prime=True

    primeNums.append(2)
    primeNums.append(3)

    for i in range(5,100):
        for j in range(len(primeNums)):
            if i%primeNums[j]==0:
                prime=False
        if prime:
            primeNums.append(i)
            prime=False
        else:
            prime=True

        if len(primeNums)-1==idx:
            break

    return primeNums[len(primeNums)-1]

def main():
    print(getPrimeNumber(10))
    
if __name__=="__main__":
    main()