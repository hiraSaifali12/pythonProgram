def countS(s):
    n=len(s)
    new=''
    count=1
    for i in range(n-1):
        if s[i]==s[i+1]:
            count +=1
        else:
            new=new+s[i]+str(count)
            count =1
    new=new+s[i]+str(count)
    return new
s='aabbbccccdddd'
print(countS(s))
