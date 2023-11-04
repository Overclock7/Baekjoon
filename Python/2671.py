# https://www.acmicpc.net/problem/2671

import sys
import re

input = sys.stdin.readline

p = re.compile('(100+1+|01)+')

if p.fullmatch(input().rstrip()):
    print('SUBMARINE')
else:
    print("NOISE")
