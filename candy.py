
for i in range(int(input())):
    a,b=map(int,input().split())
    
    if(a==0):
        print(0,0)
    elif(b==0):
        print(0,a)
    else:
        c=int(a/b)
        d=int(a%b)
        print(c,d)
