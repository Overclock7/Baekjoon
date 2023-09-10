# https://www.acmicpc.net/problem/10812

N,M = map(int,input().split())

List = []

for _ in range(1,N+1):
    List.append(_)

for _ in range(0,M):
    i,j,k = map(int,input().split())
    List[i-1:j] = List[k-1:j]+List[i-1:k-1]

print(*List)
