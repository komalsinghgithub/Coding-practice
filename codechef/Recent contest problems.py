test=int(input())

while test>0:
    a = int(input())
    problems=input().split()
    scount=0
    lcount=0
    for prob in problems:
        if prob=="START38":
            scount+=1 
        else:
            lcount+=1 
    
    print("{} {}".format(scount,lcount))
    test-=1