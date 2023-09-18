# https://www.acmicpc.net/submit/10814

import sys

N = int(sys.stdin.readline())
lst = []

for i in range(N):
    age, name = map(str,sys.stdin.readline().split())
    lst.append([int(age),name])

lst.sort(key=lambda x:x[0])

for a, n in lst:
    print(a,n)