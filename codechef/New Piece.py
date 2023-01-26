# Problem
# Chef's favorite game is chess. Today, he invented a new piece and wants to see its strengths.

# From a cell 
# (
# �
# ,
# �
# )
# (X,Y), the new piece can move to any cell of the chessboard such that its color is different from that of 
# (
# �
# ,
# �
# )
# (X,Y).

# The new piece is currently located at cell 
# (
# �
# ,
# �
# )
# (A,B). Chef wants to calculate the minimum number of steps required to move it to 
# (
# �
# ,
# �
# )
# (P,Q).

# Note: A chessboard is an 
# 8
# ×
# 8
# 8×8 square board, where the cell at the intersection of the 
# �
# i-th row and 
# �
# j-th column is denoted 
# (
# �
# ,
# �
# )
# (i,j). Cell 
# (
# �
# ,
# �
# )
# (i,j) is colored white if 
# �
# +
# �
# i+j is even and black if 
# �
# +
# �
# i+j is odd.

i=int(input())
for _ in range (i):
  a,b,p,q=map(int,input().split())
  if a==p and b==q :
    print(0)
  elif ( (a+b)%2==0 and (p+q)%2==0 ) or ((a+b)%2!=0 and (p+q)%2!=0):
    print(2)
  else :
    print(1)