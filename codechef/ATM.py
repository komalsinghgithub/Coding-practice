# Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 $US.

# Calculate Pooja's account balance after an attempted transaction.

n,atm=map(float,input().split())
n=int(n)
if (n+0.5<=atm and n%5==0):
    print(float(atm-n-0.5))
else:
    print(float(atm))