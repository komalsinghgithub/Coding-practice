x=int(input('enter the number'))
if (x>1):
    for i in range(2,int(x/2)+2):
        if(x%i)==0:
            print(x,'is not a prime number')
            break 
        else:
            print(x,'is a prime number')
else:
    print(x,'is not a prime number')            