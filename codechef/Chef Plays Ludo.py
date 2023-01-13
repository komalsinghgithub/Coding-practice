# Chef is playing Ludo. According to the rules of Ludo, a player can enter a new token into the play only when he rolls a 
# 6
# 6 on the die.

# In the current turn, Chef rolled the number 
# �
# X on the die. Determine if Chef can enter a new token into the play in the current turn or not.

tc=int(input( ))
while (tc):
    x=int(input( ))
    if (x==6):
        print("yes")
    else:
        print("no")
    tc=tc-1