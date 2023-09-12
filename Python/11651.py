# https://www.acmicpc.net/submit/11651

import sys

N = int(sys.stdin.readline())
loc_list =[]

for _ in range(N):
    x , y = map(int,sys.stdin.readline().split())
    loc_list.append([x,y])

loc_list.sort(key=lambda x:(x[1],x[0]))

for x, y in loc_list:
    print(f"{x} {y}")