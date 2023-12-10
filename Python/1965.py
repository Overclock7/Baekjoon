# https://www.acmicpc.net/problem/1965

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().rstrip().split()))
dp = [1 for _ in range(n)]

for i in range(n): # 상자가 i+1 개가 있을 때,
    for j in range(i):
        if lst[i] > lst[j]: # 상자[i]가 상자[j] 보다 크면
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))