
b=int(input())
x_1=b
i=0
while True:
    a=b//10+(b%10)
    b=(b%10)*10+a%10
    i+=1
    x=b
    if x==x_1:
         break
        
       
print(i)
    
