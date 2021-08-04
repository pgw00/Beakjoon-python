arr=[]
for i in range(9):
    arr.append(int(input()))
    
M=max(arr)

print(M)

N=arr.index(M)+1

print(N)


