# https://www.acmicpc.net/problem/14916

import sys
input = sys.stdin.readline

N = int(input())
coin = [100001] * (N+1)

if N <= 5:
    if N == 2 or N == 5:
        coin[N] = 1
    elif N == 4:
        coin[N] = 2
else:
    #Initial Values
    coin[2] = coin[5] = 1
    coin[4] = 2
    #Dynamic Programming
    for i in range(6,N+1):
        coin[i] = min(coin[i-2],coin[i-5]) + 1

print(coin[N] if coin[N] < 100001 else -1)

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
#         count +=  N // 5
#         break
#     N = N - 2
#     count += 1

# if count == -1 :
#     print(-1)
# else:
#     print(count)