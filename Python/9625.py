# https://www.acmicpc.net/problem/9625

import sys
input = sys.stdin.readline

N = int(input())
A = [0] * 46
B = [0] * 46

# 실제로 한번 나열해 보면 피보나치 수열이 나타난다.
A[0:2] = [0,0,1]
B[0:2] = [0,1,1]

for i in range(3,N+1):
    A[i] = A[i-1] + A[i-2]
    B[i] = B[i-1] + B[i-2]

print(A[N],B[N])

#2 (Baekjoon)

# N = int(input())
# A = [0] * 46
# B = [0] * 46

# A[0] = 1
# B[0] = 0

# for i in range(1,N+1):
#     A[i] = B[i-1]
#     B[i] = A[i-1] + B[i-1]

# print(A[N],B[N])