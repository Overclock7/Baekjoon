# https://www.acmicpc.net/problem/2839

import sys
input = sys.stdin.readline

N = int(input())
dp = [5001] * (N+1) # 3 <= N <= 5000
if N <= 4:
    dp[3] = 1
else:
    dp[3] = 1
    dp[5] = 1
    for i in range(6,N+1):
        dp[i] = min(dp[i-3],dp[i-5]) + 1

print(dp[N] if dp[N] < 5001 else -1)

#2 (Overclock0708)

# import sys
# input = sys.stdin.readline

# N = int(input())

# count = 0

# # Greedy Algorithm
# while True:
#     if N == 0:
#         break
#     elif N < 0:
#         count = -1
#         break
    
#     if N % 5 == 0:
#         count +=  N //5
#         break
#     N = N - 3
#     count += 1

# if count == -1 :
#     print(-1)
# else:
#     print(count)