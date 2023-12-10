# https://www.acmicpc.net/problem/11399

import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int,input().split()))

result = 0
#가장 작은 수는 N번, 그 다음 작은 수는 N-1번, ··· 
for p in sorted(P):
    result += p * N
    N -= 1

print(result)