# https://www.acmicpc.net/problem/2670

import sys
input = sys.stdin.readline

N = int(input())
lst = list(float(input()) for _ in range(N))
dp = [0.0] * (N)

for i in range(N):
    dp[i] = max(dp[i-1]*lst[i],lst[i])
    
print("%.3f"%max(dp))