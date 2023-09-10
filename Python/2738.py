# https://www.acmicpc.net/problem/2738

N,M = map(int,input().split())

l1 = [[0]*M for i in range(N)]
l2 = [[0]*M for i in range(N)]
l3 = [[0]*M for i in range(N)]

for i in range(N):
    l1[i] = list(map(int,input().split()))

for i in range(N):
    l2[i] = list(map(int,input().split()))

for i in range(0,N):
    for j in range(0,M):
        l3[i][j] += int(l1[i][j]) + int(l2[i][j])

for row in l3:
    for col in row:
        print(col,end=" ")
    print("")