# https://www.acmicpc.net/problem/2012

import sys
input = sys.stdin.readline

N = int(input())
lst = sorted(list(int(input()) for _ in range(N)))
result = 0

for i in range(N):
    result += abs(lst[i] - (i+1))

print(result)