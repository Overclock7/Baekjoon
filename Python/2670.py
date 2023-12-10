# https://www.acmicpc.net/problem/2670

import sys
input = sys.stdin.readline

N = int(input())
lst = list(float(input()) for _ in range(N))
dp = [0.0] * (N)

for i in range(N):
    #이전 DP 값에 현재 수 곱한 것과, 현재 수 비교
    dp[i] = max(dp[i-1]*lst[i],lst[i])
    
print("%.3f"%max(dp))