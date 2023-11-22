# https://www.acmicpc.net/problem/2491

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
maxi = [1] * N
mini = [1] * N

for i in range(1,N):
    if lst[i-1] <= lst[i]:
        maxi[i] = maxi[i-1] + 1
    else:
        maxi[i] = 1
    
    if lst[i-1] >= lst[i]:
        mini[i] = mini[i-1] + 1
    else:
        mini[i] = 1

print(max(max(maxi),max(mini)))