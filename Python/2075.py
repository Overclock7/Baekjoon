# https://www.acmicpc.net/problem/2075

import sys
import heapq
input = sys.stdin.readline

n = int(input())

h = list()

for i in range(n):
    for j in map(int,input().rstrip().split()):
        if len(h) < n:
            heapq.heappush(h,j)
        elif h[0] < j:
            heapq.heappush(h,j)
            heapq.heappop(h)

print(h[0])

