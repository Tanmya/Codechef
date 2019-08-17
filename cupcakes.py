#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tanmya
#
# Created:     10/08/2019
# Copyright:   (c) Tanmya 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
def main():
    pass

if __name__ == '__main__':
    main()
for _ in range(int(input())):
    a=int(input())

    t=math.sqrt(a)
    if int(t + 0.5) ** 2 == a:
        r=0
    else:
        l=[]
        for i in range(1, math.ceil((a+1)/2)):
           if a % i == 0:
            l.append(i)
        if len(l)==1:
            r=a-1
        else:
            r=l[math.ceil(len(l)/2)]-l[math.ceil(len(l)/2)-1]
    print(r)