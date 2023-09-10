# https://www.acmicpc.net/problem/5597

import sys

n = 30
l = list(range(1,31))

for i in range(1,29):
    l.remove(int(input()))
    
print(min(l))
print(max(l))
