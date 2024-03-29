# https://www.acmicpc.net/problem/13699

import sys
input = sys.stdin.readline

n = int(input())
t = [0 for _ in range(36)]

t[0] = 1
t[1] = 1
t[2] = 2
t[3] = 5

#점화식을 잘 보자!
for i in range(4,n+1):
    for j in range(i):
        t[i] += t[j]*t[i-j-1]

print(t[n])
