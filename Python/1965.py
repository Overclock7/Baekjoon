# https://www.acmicpc.net/problem/1965

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().rstrip().split()))
dp = [1 for _ in range(n)]


for i in range(n):
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))