T = int(input())
for t in range(T):
    # print(f'Test {t+1}')
    N, Y = map(int, input().split())
    A = map(int, input().split())
    R = 0
    for a in A: R |= a
    D = R^Y
    print(D if D|R == Y else -1)