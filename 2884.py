x,y=map(int,input().split())

if(y<45 and x>0):
    print(x-1,y+15)
elif(y>44):
    print(x,y-45)    
else:
    print(23,y+15)
