#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tanmya
#
# Created:     08/08/2019
# Copyright:   (c) Tanmya 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
n=int(input())
l=list(map(int,input().split()))
s=sum(l)
ns=(n*(n-1))/2
if n==1:
    if s>1:
        print("NO")
    else:
        print("YES")
else:
    if s==ns:
        print("YES")
    else:
        print("NO")
