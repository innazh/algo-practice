#Return 1 if the second word is an anagram of the first.
#Ignore capitalisation and spaces
def isAnagram(word, anagram):
    a = "".join(sorted(anagram.replace(" ", "").lower()))
    w = "".join(sorted(word.replace(" ", "").lower()))
    
    if len(w)!=len(a):
        return 0
    res = 1
    for i in range(len(w)):
        if w[i]!=a[i]:
            res=0
            break

    return res

def main():
    print(isAnagram("I like cats", "Stac kileI"))
    print(isAnagram("I like cats", "Stac kilrI"))
    
if __name__=="__main__":
    main()