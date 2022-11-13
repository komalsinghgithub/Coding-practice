x=int(input('enter the number'))
y=int(input('enter the number'))
z=int(input('enter the number'))
if (x>y and x>z):
    print(x ,'is greater than' , y ,"and",z )
elif (y>=x and y>=z):
    print(y ,'is greater than', x ,'and',z )
else:
    print (z ,'is greater than',y ,'and',x)


