#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tanmya
#
# Created:     11/08/2019
# Copyright:   (c) Tanmya 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
a=int(input())
b=0
c=0
if(a==0):
    print("yes")
else:
    b=int(a/6)
    b=b*6

    for i in range(a+1):
        b=b+1
        if(b>=a):
            break
        else:
            b=b+2
            if(b>=a):
                break
            else:
                b=b+3
                if(b>=a):
                    break
    if(b==a):
        print("yes")
    else:
        print("no")