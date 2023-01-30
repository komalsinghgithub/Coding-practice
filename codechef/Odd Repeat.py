
# Problem
# Chef has an array consisting of 
# �
# +
# �
# −
# 1
# N+K−1 integers. The array contains only the first 
# �
# N positive odd numbers. Each number appears exactly once, except for one number which appears exactly 
# �
# K times. The sum of integers in Chef's array is equal to 
# �
# S.

# For example, for 
# �
# =
# 3
# N=3, 
# �
# =
# 2
# K=2, the possible arrays could be 
# [
# 1
# ,
# 1
# ,
# 3
# ,
# 5
# ]
# [1,1,3,5], 
# [
# 3
# ,
# 1
# ,
# 3
# ,
# 5
# ]
# [3,1,3,5], 
# [
# 5
# ,
# 3
# ,
# 5
# ,
# 1
# ]
# [5,3,5,1]. For 
# �
# =
# 1
# N=1, 
# �
# =
# 3
# K=3, there is only one possible array: 
# [
# 1
# ,
# 1
# ,
# 1
# ]
# [1,1,1].

# Chef gives you three integers 
# �
# N, 
# �
# K and 
# �
# S and asks you to find the only element which appears 
# �
# K times in his array.

# It is guaranteed that for the given input, there exists a valid array consisting of 
# �
# +
# �
# −
# 1
# N+K−1 elements with a sum exactly equal to 
# �
# S.
t = int(input())
for x in range(t):
    
    
    n,k,s=map(int,input().split())
    a=list(range(1,n*2,2))
    d = sum(a)
    for x in range(len(a)):
      z = a[x]*(k-1) + d
      if z == s:
        print(a[x])