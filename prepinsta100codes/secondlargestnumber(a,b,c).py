a,b,c=map(int,input().split(" "))
if(a<b<c or c<b<a):
    print(b)
if(b<c<a or a<c<b):
    print(c)
if(b<a<c or c<a<b):
    print(a)