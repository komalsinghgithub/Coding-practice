for _ in range(int(input())):
    n1=int(input())
    s1=list(map(int,input().split()))
    d={}
    for i in s1:
        if(i not in d.keys()):
            d[i]=1
        else:
            d[i]+=1
    flag=1
    for i in d.keys():
        if(d[i]%2!=0):
            flag=0
            break
    if(flag==0):
        print("NO")
    else:
        print("YES")