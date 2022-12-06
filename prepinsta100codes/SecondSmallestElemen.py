# Find Second Smallest Element in an Array :
def findsecmax(array):
    a=sorted(array)
    return a[1]
array=[2,7,98,1,-6,56,6]
print(findsecmax(array))