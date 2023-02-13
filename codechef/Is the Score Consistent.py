
# Problem
# Chef is watching a football match. The current score is 
# �
# :
# �
# A:B, that is, team 
# 1
# 1 has scored 
# �
# A goals and team 
# 2
# 2 has scored 
# �
# B goals. Chef wonders if it is possible for the score to become 
# �
# :
# �
# C:D at a later point in the game (i.e. team 
# 1
# 1 has scored 
# �
# C goals and team 
# 2
# 2 has scored 
# �
# D goals). Can you help Chef by answering his question?


for i in range(int(input())):
    a,b=map(int,input().split())
    c,d=map(int,input().split())
    if(a<=c and b<=d):
        print("possible")
    else:
        print("impossible")