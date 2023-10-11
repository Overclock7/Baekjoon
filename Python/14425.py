# https://www.acmicpc.net/problem/14425

import sys
input = sys.stdin.readline

N, M = map(int,input().strip().split())

String = set()
Check = list()

for _ in range(N):
    String.add(input().strip())

for _ in range(M):
    Check.append(input().strip())

print(sum(1 for c in Check if c in String))