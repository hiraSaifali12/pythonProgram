#=====sort the list without using sort functions===============
list=[1,23,2,33,31,38]
n=len(list)
for i in range(n):
    for j in range(i+1 ,n):
        if list[i]> list[j]:
            
           list[i],list[j]= list[j],list[i]
print(list)   
