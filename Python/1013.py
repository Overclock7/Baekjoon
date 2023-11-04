# https://www.acmicpc.net/problem/1013

import sys
import re

input = sys.stdin.readline

p = re.compile('(100+1+|01)+')
for _ in range(int(input())):
    if p.fullmatch(input().rstrip()):
        print('YES')
    else:
        print("NO")