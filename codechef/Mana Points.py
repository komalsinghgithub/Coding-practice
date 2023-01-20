# Problem
# Chef is playing a mobile game. In the game, Chef's character Chefario can perform special attacks. However, one special attack costs 
# �
# X mana points to Chefario.

# If Chefario currently has 
# �
# Y mana points, determine the maximum number of special attacks he can perform.

t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x<=y:
        print(int(y/x))
    else:
        print(0)