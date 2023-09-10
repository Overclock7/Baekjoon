# https://www.acmicpc.net/problem/10813

N,M = map(int,input().split())

L = []

for i in range(1,N+1):
    L.append(i)

for i in range(0,M):
    a,b = map(int,input().split())
    temp = L[a-1]
    L[a-1] = L[b-1]
    L[b-1] = temp

print(*L)

