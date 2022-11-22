x=int(input())
value=64
for i in range(1,x+1):
    for j in range(1,i+1):
        print(chr(value+j),end=" ")
    print() 
