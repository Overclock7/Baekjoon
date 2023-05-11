import sys

N,X = map(int,sys.stdin.readline().split())

L = list(map(int,sys.stdin.readline().split()))
R = list()

for i in range(0,N):
    if(L[i]<X):
        R.append(L[i])

for i in R:
    print(i,end=' ')