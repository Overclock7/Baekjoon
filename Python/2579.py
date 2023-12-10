# https://www.acmicpc.net/problem/2579

import sys

n = int(input())
step = [0] + [int(input()) for i in range(n)]
lst = [0] * (n+1)

if n >= 1:
    lst[1] = step[1]
if n >= 2:
    lst[2] = step[1] + step[2]

# 연속된 3계단 밟는 경우를 빼고 DP를 함
for i in range(3,n+1):
    lst[i] = max(lst[i-2],lst[i-3]+step[i-1]) + step[i]

print(lst[n])
