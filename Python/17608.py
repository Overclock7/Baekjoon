# https://www.acmicpc.net/problem/17608

import sys

N = int(sys.stdin.readline())
count = 0
longest = 0

lst = [int(sys.stdin.readline()) for _ in range(N)]
lst_reverse = lst[::-1]

for i in lst_reverse:
    if longest < i :
        longest = i
        count += 1

print(count)