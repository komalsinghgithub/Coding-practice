# Problem
# Chef appeared for a placement test.

# There is a problem worth 
# �
# X points. Chef finds out that the problem has exactly 
# 10
# 10 test cases. It is known that each test case is worth the same number of points.

# Chef passes 
# �
# N test cases among them. Determine the score Chef will get.

# NOTE: See sample explanation for more clarity.

t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    n=x/10
    a=n*y
    print(int(a))