# https://www.acmicpc.net/problem/9996

import sys
import re

input = sys.stdin.readline

T = int(input())
r = input().rstrip().replace('*','[a-z]*')

p = re.compile('^'+r+'$')
for _ in range(T):
    s = input().rstrip()
    m = p.match(s)
    if m:
        print('DA')
    else:
        print('NE')
