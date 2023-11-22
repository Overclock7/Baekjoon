# https://www.acmicpc.net/problem/25214

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
dp = [0] * N

mini = lst[0] # lst[i]가 들어오기 전 가장 작은 수
dp[0] = 0 # lst[0] 밖에 없으므로 초기값은 0
for i in range(1,N):
    dp[i] = max(dp[i-1],lst[i]-mini)
    mini = min(mini,lst[i])

print(*dp)