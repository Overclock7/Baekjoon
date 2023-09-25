# https://www.acmicpc.net/problem/9012

import sys

N = int(sys.stdin.readline())

for i in range(N):
    PS = sys.stdin.readline().rstrip()

    L = 0
    R = 0
    FLAG = 1

    for P in PS:
        if "(" == P :
            L += 1
        elif ")" == P:
            if L > R:
                R += 1
            elif L <= R:
                FLAG = 0
                break
    
    if L != R:
        FLAG = 0

    if FLAG == 1:
        print("YES")
    else:
        print("NO")

# Baekjoon

# from sys import stdin

# n = int(input())
# for _ in range(n):
#     tmp = stdin.readline().strip()
#     while tmp.count('()') != 0:
#         tmp = tmp.replace('()', '')
#     if len(tmp) == 0:
#         print("YES")
#     else:
#         print("NO")