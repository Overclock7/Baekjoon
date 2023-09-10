# https://www.acmicpc.net/problem/2775

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    apt = [[0]*(n+1) for _ in range(k+1)]

    for i in range(1,n+1):
        apt[0][i] = i

    for i in range(k+1):
        apt[i][1] = 1

    for i in range(1,k+1):
        for j in range(1,n+1):
            apt[i][j] = apt[i-1][j] + apt[i][j-1]

    print(apt[k][n])