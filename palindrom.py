
def pal(s):
    n=len(s)
    first,last=0,n-1
    while(first<=last):
        if s[first]==s[last]:
            first+=1
            last-=1
        else:
            return False
    return True
    
def pal2(s):
    n=len(s)
    temp=s[::-1]
    for i in range(n):
        if temp==s:
            return True
        else:
            return False

            
def pal3(s):
    n=len(s)
    for i in range(n):
        if s[i]==s[n-i-1]:
            return True 
        else:
            return False
            
def pal4(s):
    temp=''.join(reversed(s))
    if s==temp:
        return True
    else:
        return False
#------------------------------------------
def pal(num):
    
    temp=num
    rev=0
    while(temp>0):
        dig=temp%10
        rev=(rev*10)+dig
        temp=temp//10
        
    if num==rev:
        return True
    else:
        return False
#-------------------------------------------------------
s="nitin"
print(pal(s))
print(pal12(s))        
print(pal3(s))
print(pal4(s))
#--------------------number---------palindrom---------------
num=12322
print(pal(num))
