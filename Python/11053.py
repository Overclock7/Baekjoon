# https://www.acmicpc.net/problem/11053

import sys
input = sys.stdin.readline

n = int(input().rstrip())
lst = [0] + list(map(int,input().rstrip().split()))
dp = [0] + [1 for _ in range(n)]

for i in range(1,n+1):
    for j in range(1,i+1):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))

#2 (ericeric00)

# import sys
# input = sys.stdin.readline

# def LCS(X,Y):
#     m = len(X)
#     n = len(Y)
#     dp = [[None]*(n+1) for i in range(m+1)]

#     for i in range(m+1):
#         for j in range(n+1):
#             if i == 0 or j == 0:
#                 dp[i][j] = 0
#             elif X[i-1] == Y[j-1]:
#                 dp[i][j] = dp[i-1][j-1] + 1
#             else:
#                 dp[i][j] = max(dp[i][j-1],dp[i-1][j])
#     return dp[m][n]

# N = int(input())
# array = list(map(int,input().split()))
# pattern = [i for i in range(1, max(array) + 1)]
# print(LCS(pattern,array))