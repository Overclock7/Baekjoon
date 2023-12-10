# https://www.acmicpc.net/problem/25644

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().rstrip().split()))
dp = [0] * 200001

mini = lst[0]
for i in range(1,N):
    mini = min(mini,lst[i]) # 가장 낮은 주가
    dp[i] = max(dp[i-1],lst[i]-mini)

print(max(dp))