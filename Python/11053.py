# https://www.acmicpc.net/problem/11053

import sys
input = sys.stdin.readline

n = int(input().rstrip())
lst = [0] + list(map(int,input().rstrip().split()))
dp = [0] + [1 for _ in range(n)]

for i in range(1,n+1):
    for j in range(1,i+1):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))