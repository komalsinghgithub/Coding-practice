# Ezio can manipulate at most 
# �
# X number of guards with the apple of eden.

# Given that there are 
# �
# Y number of guards, predict if he can safely manipulate all of them.

# cook your dish here
T = int(input())
while (T > 0):
    a, b = map(int, input().split())
    
    if (a >= b):
        print("Yes")
    else:
        print("No")
        
    T = T - 1 