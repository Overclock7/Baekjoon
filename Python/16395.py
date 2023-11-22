# https://www.acmicpc.net/problem/16395

import sys
input = sys.stdin.readline

N, K = map(int,input().split())
dp = [[1 for _ in range(N)] for _ in range(N)]

for i in range(2,N):
    for j in range(1,i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        
print(dp[N-1][K-1])

#2 (Overclock0708)
# import sys
# input = sys.stdin.readline

# N, K = map(int,input().split())
# factorial = [1] * (N+1)
# for i in range(1,N+1):
#     factorial[i] = factorial[i-1] * i

# print(factorial[N-1] // (factorial[K-1] * factorial[N-K]))