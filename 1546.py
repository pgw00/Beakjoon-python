a=int(input())
arr=[]
arr=list(map(int,input().split()))

M=max(arr)

for i in range(a):
    arr[i]=arr[i]/M*100

s=sum(arr)
print(s/a)
    

