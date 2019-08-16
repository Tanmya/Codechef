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
for _ in range(int(input())):
    n,a,b,k=map(int,input().split())
    t=1
    c=0
    for i in range(n):
        if (t%a==0 and t%b==0) or(t%a!=0 and t%b!=0):

            t=t+1
        elif(t%a==0 and t%b!=0) or (t%b==0 and t%a!=0):
            c=c+1
            t=t+1
    if (c>=k):
        print("Win")
    else:
        print("Lose")



