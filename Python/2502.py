# https://www.acmicpc.net/problem/2502

import sys
input = sys.stdin.readline

N, K = map(int,input().split())
dp = [0] * N

dp[1] = dp[2] = 1

for i in range(3,N):
    dp[i] = dp[i-2] + dp[i-1]

flag = 0

for a in range(1,K):
    for b in range(a,K):
        if K == a * dp[N-2] + b * dp[N-1]:
            print(a)
            print(b)
            flag = 1
            break
    if flag:
        break