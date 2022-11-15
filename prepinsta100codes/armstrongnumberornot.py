n=int(input('enter the number: '))
x=str(n)
sum=0
for i in x:
    sum=sum+int(i)**3
if (sum==n):
    print("armstrong number")
else:
    print("not a armstrong number")