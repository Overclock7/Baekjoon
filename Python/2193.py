# https://www.acmicpc.net/problem/2193

import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 91

dp[1] = 1
dp[2] = 1

#피보나치 수열을 보임
for i in range(3,N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])