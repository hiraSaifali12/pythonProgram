def fizzBuzz(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print("fizzbuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(i) 
#===============using dictionary=============================  
  
def fizzBuzzDic(n):
    d={3:'fizz',5:'buzz'}
    for i in range(1,n+1):
        result= ''
        for k,v in d.items():
            if i%k==0:
                result += v
        if not result :
            result= i
        print(result)
             
fizzBuzz(15)          
             
fizzBuzzDic(20)  
