# https://www.acmicpc.net/problem/10818

import sys

n = int(sys.stdin.readline())

l = list(map(int,sys.stdin.readline().split()))

max = max(l)
min = min(l)

print(min,max)