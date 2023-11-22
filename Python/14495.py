# https://www.acmicpc.net/problem/14495

import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)

if N <= 3:
    dp[N] = 1
else:
    dp[1] = dp[2] = dp[3] = 1
    for i in range(4,N+1):
        dp[i] = dp[i-1] + dp[i-3]

print(dp[N])