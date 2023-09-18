# https://www.acmicpc.net/problem/118

import sys

N = int(sys.stdin.readline())
lst = list()

for i in range(N):
    lst.append(sys.stdin.readline().rstrip())

lst = list(set(lst))

lst.sort(key = lambda x : (len(x),x))

for s in lst:
    print(s)