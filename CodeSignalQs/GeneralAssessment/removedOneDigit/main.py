#how many ways can we remove 1 digit from either array so that s<t lexicographically
#note: doesn't pass some edge cases
def removeOneDigit(a):
    counter=0
    for i in range(len(s)):
        if s[i].isdigit():
            trys = s.replace(s[i],'')
            if trys<t:
                counter+=1
    for j in range(len(t)):
        if t[j].isdigit():
            trys = t.replace(t[j],'')
            if s<trys:
                counter+=1
    return counter