# https://www.acmicpc.net/problem/16953

import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int,input().split())
result = -1
queue = deque([(a,1)]) #BFS 탐색

while queue:
    i, count = queue.popleft()
    if i == b:
        result = count
        break
    if i*2 <= b:
        queue.append((i*2, count+1)) # type: ignore
    if int(str(i)+'1') <= b:
        queue.append((int(str(i)+'1'), count+1)) # type: ignore

print(result)

# 2 (baekjoon)

# a,b = map(int,input().split())
#
# result =1
# while a!=b:
#     result += 1
#     temp = b
#
#     if b % 10 ==1:
#         b //= 10
#     elif b % 2==0:
#         b //= 2
#
#     if temp == b: #만들 수 없는 경우
#         print(-1)
#         break
# else:
#     print(result)