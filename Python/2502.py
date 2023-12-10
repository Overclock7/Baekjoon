# https://www.acmicpc.net/problem/2502

import sys
input = sys.stdin.readline

D, K = map(int,input().split())
dp = [0] * D

# 피보나치 생성
dp[1] = dp[2] = 1
for i in range(3,D):
    dp[i] = dp[i-2] + dp[i-1]

# 곱해지는 수가 피보나치 성질을 보임
# Day(3) = 1a + 1b
# Day(4) = 1a + 2b
# Day(5) = 2a + 3b
# Day(6) = 3a + 5b

for a in range(1,K): # a 는 첫째 날 준 떡 갯수
    for b in range(a,K): # b 는 둘째 날 준 떡 갯수
        if K == a * dp[D-2] + b * dp[D-1]:
            print(a)
            print(b)
            exit(0)