# https://www.acmicpc.net/problem/2491

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
maxi = [1] * N
mini = [1] * N

for i in range(1,N):
    if lst[i-1] <= lst[i]: # 커지면은 1을 더함
        maxi[i] = maxi[i-1] + 1
    else: #흐름이 끊김
        maxi[i] = 1
    
    if lst[i-1] >= lst[i]: # 작아지면 1을 더함
        mini[i] = mini[i-1] + 1
    else: # 흐름이 끊김
        mini[i] = 1

print(max(max(maxi),max(mini)))