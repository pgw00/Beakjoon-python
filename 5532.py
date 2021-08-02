L=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

if b%d==0:
    m=b//d
else:
    m=b//d+1

if c%e==0:
    n=c//e
else:
    n=c//e+1
k=max(m,n)

print(L-k)


