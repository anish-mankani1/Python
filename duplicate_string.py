def find_duplicate(s):
    n=len(s)
    print(n)
    l=[]
    for  i in range(n):
        for j in range(i+1,n):
            if s[i]==s[j] and  s[i] not in l:
                l.append(s[i])
    print(l)

find_duplicate("programmings")