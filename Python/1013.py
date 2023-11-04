# https://www.acmicpc.net/problem/1013

import sys
import re

input = sys.stdin.readline

p = re.compile('(100+1+|01)+')
for _ in range(int(input())):
    if p.fullmatch(input().rstrip()): #전체 문자열 체크
        print('YES')
    else:
        print("NO")