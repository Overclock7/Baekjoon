# https://www.acmicpc.net/problem/2562

import sys

n = 9

l = list()
location = 0

m = 0

for i in range(0,n):
    l.append(int(sys.stdin.readline()))
    m = max(l)
    for j in range(0,i+1):
        if (m == l[j]):
            location = j+1

print("{}\n{}".format(m,location))