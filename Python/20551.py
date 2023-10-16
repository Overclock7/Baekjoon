# https://www.acmicpc.net/problem/20551

# 1

import sys
input = sys.stdin.readline

n, m = map(int,input().rstrip().split())

array_A = list()

for _ in range(n):
    array_A.append(int(input()))

array_B = sorted(array_A)
dict_B = dict()

for k,v in enumerate(array_B):
    if v not in dict_B:
        dict_B[v] = k

for _ in range(m):
    x = int(input())
    if x in dict_B:
        print(dict_B[x])
    else:
        print(-1)

# 2 (Overclock0708)
# import sys
# import heapq
# input = sys.stdin.readline

# def Heapsort(l):
#     heapq.heapify(l)
#     return [heapq.heappop(l) for _ in range(len(l))]

# n, m = map(int,input().rstrip().split())

# array_A = list()
# array_B = list()

# for _ in range(n):
#     array_A.append(int(input()))

# array_B = Heapsort(array_A)

# dict_B = dict()

# for k,v in enumerate(array_B):
#     if v not in dict_B:
#         dict_B[v] = k

# for _ in range(m):
#     x = int(input())
#     if x in dict_B:
#         print(dict_B[x])
#     else:
#         print(-1)