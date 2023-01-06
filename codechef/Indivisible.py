# Alice thinks Bob has very weak math skills.
# Alice gave Bob three numbers A, B,A,B, and CC and challenged him to find any positive integer KK strictly less than 100100 such that none of the three numbers are divisible by KK.

# Help Bob find one such integer KK.

# Under the given constraints, a valid KK will always exist.

tc=int(input())
while(tc):
    a,b,c=map(int,input().split(" "))
    for i in range(2,101):
        if (a%i!=0 and b%i!=0 and c%i!=0):
            print(i)
            break
    tc=tc-1
