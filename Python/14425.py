# https://www.acmicpc.net/problem/14425

import sys

N , M = map(int,sys.stdin.readline().split())

list_N = []
list_M = []
count = 0

for i in range(N):
    list_N.append(sys.stdin.readline())

for j in range(M):
    list_M.append(sys.stdin.readline())

for n in list_M:
    if n in list_N:
        count += 1

print(count)