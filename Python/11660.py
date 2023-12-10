# https://www.acmicpc.net/problem/11660

import sys
input = sys.stdin.readline

N,M = map(int,input().rstrip().split())
arr = [list(map(int,input().rstrip().split())) for _ in range(N)]
dp = [[0] * (N+1) for _ in range(N+1)]

# (1,1)부터 (i,j)까지의 누적합
for i in range(1,N+1):
    for j in range(1,N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + arr[i-1][j-1] - dp[i-1][j-1]

for _ in range(M):
    x1,y1,x2,y2 = map(int,input().rstrip().split())
    print(dp[x2][y2]-dp[x2][y1-1]-dp[x1-1][y2]+dp[x1-1][y1-1])