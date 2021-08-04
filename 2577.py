a=int(input())
b=int(input())
c=int(input())
M=a*b*c

for i in range(10):
    print(list(str(M)).count(str(i)))
