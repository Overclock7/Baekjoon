# https://www.acmicpc.net/problem/15552

import sys

n = int(sys.stdin.readline())

for i in range(0,n):
    print(sum(list(map(int,sys.stdin.readline().split()))))