# https://www.acmicpc.net/problem/9342

import re

T = int(input())
p = re.compile("[A-F]{0,1}A+F+C+[A-F]{0,1}$")
for i in range(T):
    s = input()
    if p.match(s):
        print('Infected!')
    else:
        print('Good')