# https://www.acmicpc.net/problem/8393

import sys

n = int(sys.stdin.readline())

total = 0

for i in range(0,n+1):
    total += i

print(total)