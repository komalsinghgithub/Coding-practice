# Problem
# A tutorial for this problem is now available on our blog. Click here to read it.
# You are asked to calculate factorials of some small positive integers.

def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input())
for i in range(n):
    num=int(input())
    print(factorial(num))
