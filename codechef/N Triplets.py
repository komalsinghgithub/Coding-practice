# Alice is still not satisfied with Bob's math skills so she gave him a new challenge.

# Given a positive integer NN, find any 33 distinct positive integers A, B, CA,B,C such that:

# The product of any two of these 33 integers is a divisor of NN.
# The product of all three integers is a multiple of NN.
# If multiple solutions exist, you may print any of them.
# Print -1−1 if no solution exists.

a=int(input())
for tc in range(a):
    z=int(input())
    i=2
    answer=1
    while((i*i)<=z):
        if(z%i==0) and (i!=(z/i)):
            answer=0
            break
        i=i+1
    if answer:
        print(-1)
    else:
        print(1,i,z//i)