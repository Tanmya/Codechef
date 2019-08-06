#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tanmya
#
# Created:     04/08/2019
# Copyright:   (c) Tanmya 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from array import*
def main():
    pass

if __name__ == '__main__':
    main()
t=int(input())
for k in range(t):
    s=int(input())
    a = list(map(int, input().split(' ')))
    c=1

    for i in range(len(a)-1):
        if a[i+1]<=a[i]:
            c+=1
        else:
            a[i+1]=a[i]
    print(c)



