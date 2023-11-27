# https://www.acmicpc.net/problem/16953

import sys
from collections import deque
input = sys.stdin.readline

A, B = map(int,input().split())
result = -1
queue = deque([(A,1)])

while queue:
    a, count = queue.popleft()
    if a == B:
        result = count
        break
    if a*2 <= B:
        queue.append((a*2, count+1))
    if int(str(a)+'1') <= B:
        queue.append((int(str(a)+'1'), count+1))

print(result)