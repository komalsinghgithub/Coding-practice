# Problem
# Chef has the binary representation 
# �
# S of a number 
# �
# X with him. He can modify the number by applying the following operation exactly once:

# Make 
# �
# :
# =
# �
# ⊕
# ⌊
# �
# 2
# �
# ⌋
# X:=X⊕⌊ 
# 2 
# Y
 
# X
# ​
#  ⌋, where 
# (
# 1
# ≤
# �
# ≤
# ∣
# �
# ∣
# )
# (1≤Y≤∣S∣) and 
# ⊕
# ⊕ denotes the bitwise XOR operation.
# Chef wants to maximize the value of 
# �
# X after performing the operation. Help Chef in determining the value of 
# �
# Y which will maximize the value of 
# �
# X after the operation.

for i in range(int(input())):
    n=int(input())
    s=input()
    i=1
    while(i<n and s[i]=='1' ):
        i+=1
    print(i)