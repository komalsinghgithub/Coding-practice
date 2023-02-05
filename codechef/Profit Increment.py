# Problem
# Chef recently started selling a special fruit.
# He has been selling the fruit for 
# �
# X rupees (
# �
# X is a multiple of 
# 100
# 100). He earns a profit of 
# �
# Y rupees on selling the fruit currently.

# Chef decided to increase the selling price by 
# 10
# %
# 10%. Please help him calculate his new profit after the increase in selling price.

# Note that only the selling price has been increased and the buying price is same.

tc=int(input())
while(tc):
    x,y=map(int,input().split( ))
    z=(x//100)*10
    w=x-y
    v=x+z
    print(v-w)
    
    tc=tc-1