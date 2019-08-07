#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tanmya
#
# Created:     05/08/2019
# Copyright:   (c) Tanmya 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
for _ in range(int(input())):
    x=list(map(str,input()))
    y=list(map(str,input()))
    c=0
    k=0
    l=len(x)
    z = list( dict.fromkeys(x) )

    for i in range(len(z)):
        for j in range(len(y)):
            if z[i]==y[j]:
                c+=1
    print(c)