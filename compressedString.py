#==============for loop========================
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

#===============while loop================
def com(s):
    n=len(s)
    i=0
    new=''
    
    while(i<n-1):
        count=1
        while(i<n-1 and s[i]==s[i+1]):
            count+=1
            i+=1
        i+=1        
    
        new=new+s[i-1]+str(count)
    
    return new
#=====================================================    

    

s='aabbbccccdddd'
print(countS(s))

#==========================================================
s="aabbbccccddddd" 
print(com(s))
