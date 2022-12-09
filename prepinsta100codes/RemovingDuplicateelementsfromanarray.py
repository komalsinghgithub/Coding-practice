def removeduplicates( arr, n):
    if n == 0 or n == 1:
        return n
    j = 0
    for i in range(0, n-1):
        if arr[i] != arr[i+1]:
            arr[j] = arr[i]
            j += 1
    arr[j] = arr[n-1]
    j += 1

    return j
arr = [10, 20, 20, 30, 40, 40, 40, 50, 50]
n = len(arr)
n = removeduplicates(arr, n)
for i in range(n):
    print ("%d"%(arr[i]), end = " ")