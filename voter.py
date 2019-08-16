#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Tanmya
#
# Created:     06/08/2019
# Copyright:   (c) Tanmya 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
x,y,z=map(int,input().split())

xa=[]
ya=[]
za=[]
res=[]
for i in range(x):
    xa.append(int(input()))
for i in range(y):
    ya.append(int(input()))
for i in range(z):
    za.append(int(input()))

if len(xa)>=len(ya) and len(za)>=len(ya):
    for i in range(len(xa)-1,len(ya)-1,-1):
        del xa[i]
    for i in range(len(za)-1,len(ya)-1,-1):
        del za[i]
if len(xa)>=len(za) and len(ya)>=len(za):
    for i in range(len(xa)-1,len(za)-1,-1):
        del xa[i]
    for i in range(len(ya)-1,len(za)-1,-1):
        del ya[i]
if len(za)>=len(xa) and len(ya)>=len(xa):
    for i in range(len(za)-1,len(xa)-1,-1):
        del za[i]
    for i in range(len(ya)-1,len(xa)-1,-1):
        del ya[i]

for i in range(len(xa)):
    if xa[i]==ya[i] or xa[i]==za[i]:
        res.append(xa[i])
    if ya[i]==xa[i] or ya[i]==za[i]:
        res.append(ya[i])
    if za[i]==xa[i] or za[i]==ya[i]:
        res.append(za[i])
print(len(res))
for i in range(len(res)):
    print(res[i])

