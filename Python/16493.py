# https://www.acmicpc.net/problem/16493

import sys
input = sys.stdin.readline

# 0/1 Knapsack Problems
# N = Max Days(knapsack) / M = Number of Items
N,M = map(int,input().split())

# Item = [ Day(weight) , Page(benefit) ]
I = [[0,0]]
for _ in range(M):
    temp = list(map(int,input().split()))
    I.append(temp)

# Benefit[Number of Item][Max Days]
B = [[0 for _ in range(N+1)] for _ in range(M+1)]

for i in range(1,M+1): # Number of Items
    for d in range(1,N+1): # Max Days(Knapsack)
        if I[i][0] <= d:
            B[i][d] = max(B[i-1][d],B[i-1][d-I[i][0]] + I[i][1])
        else:
            B[i][d] = B[i-1][d]

print(B[M][N])

