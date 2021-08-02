def Y(a):
    if a==0:
        return 0
    ys=(a//30)*10+10
    return ys

def M(b):
    if b==0:
        return 0
    ms=(b//60)*15+15
    return ms






x=int(input())
a=0
b=0
arr=list(map(int,input().split()))
for i in arr:
    y=Y(i)
    m=M(i)
    a+=y
    b+=m
    
        
      
                
    
if a<b:
    print('Y',a)    
elif a>b:
    print('M',b)
else:
    print('Y','M',a)
