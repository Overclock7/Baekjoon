# https://www.acmicpc.net/problem/9657

import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 1001

dp[1] = 1 # 상근
dp[2] = 0 # 창영
dp[3] = 1
dp[4] = 1

# 상근이 선수 일 경우
for i in range(5,N+1):
    if dp[i-1] == 0 or dp[i-3] == 0 or dp[i-4] == 0: # 돌이 1,3,4개를 뺏을 때, 창영이 이기는 경우
        dp[i] = 1 # 이때 상근이 이김
    else:
        dp[i] = 0

print('SK' if dp[N] else 'CY')