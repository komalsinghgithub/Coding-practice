# By function call
def sumarray(nums):
    # write your code here
    sum=0
    for i in range (len(nums)):
        sum=sum+nums[i]
    return sum
print(sumarray([3,6,8,9,4,6]))


# Without function
x=int(input())
array=list(map(int,input().split(" ")))
sum=0
for i in range(x):
    sum=sum+array[i]
print(sum)










