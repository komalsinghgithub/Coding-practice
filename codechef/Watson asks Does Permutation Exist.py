# Problem
# Read problems statements in Mandarin Chinese, Russian and Vietnamese as well.
# Watson gives an array A of N integers A1, A2, ..., AN to Sherlock. He wants Sherlock to reorganize the array in a way such that no two adjacent numbers differ by more than 1.

# Formally, if reorganized array is B1, B2, ..., BN, then the condition that | Bi - Bi + 1 | ≤ 1, for all 1 ≤ i < N(where |x| denotes the absolute value of x) should be met.

# Sherlock is not sure that a solution exists, so he asks you.
def check(l):
    for i in range(len(l)-1):
        if abs(l[i]-l[i+1])>1:
            return "NO"
    return "YES"
t=int(input())
for i in range(t):
    n=int(input())
    l=[int(i) for i in input().split(' ',n-1)]
    l.sort()
    print(check(l))