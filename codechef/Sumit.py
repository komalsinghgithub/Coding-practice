# Bob received an assignment from his school: he has two numbers AA and BB, and he has to find the sum of these two numbers.
# Alice, being a good friend of Bob, told him that the answer to this question is CC.
# Bob doesn't completely trust Alice and asked you to tell him if the answer given by Alice is correct or not.
# If the answer is correct print "YES", otherwise print "NO" (without quotes).

tc=int(input())
while(tc):
    a,b,c= map(int,input().split(" "))
    if (a+b==c):
        print("yes")
    else:
        print("no")
    tc=tc-1