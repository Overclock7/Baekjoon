
N,M = map(int,input().split())

L = []

for i in range(1,N+1):
    L.append(i)

for i in range(0,M):
    a,b = map(int,input().split())
    L = L[0:a-1]+L[a-1:b][::-1]+L[b:]

print(" ".join(str(l) for l in L))