def Han(n):
    y=0
    for i in range(1,n+1):
        arr=list(map(int,str(i)))
        if i < 100:
            y+=1
        elif arr[0]-arr[1]==arr[1]-arr[2]:
            y+=1
    return y
        
        
        










n=int(input())
print(Han(n))
