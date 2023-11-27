# https://www.acmicpc.net/problem/11399

import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int,input().split()))

result = 0
for p in sorted(P):
    result += p * N
    N -= 1

print(result)