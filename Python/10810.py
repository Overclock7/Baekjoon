# https://www.acmicpc.net/problem/10810

N,M = map(int,input().split())

list = []

for i in range(0,N):
    list.append(0)

for a in range(0,M):
    i,j,k = map(int,input().split())
    for b in range(i-1,j):
        list[b] = k

for i in range(0,N):
    print(list[i],end=" ")