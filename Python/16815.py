# https://www.acmicpc.net/problem/16815

import sys

S = sys.stdin.readline().strip()
count = 0

while S.count("()") != 0:
    S = S.replace("()","")

S = S.replace("*","")

while S.count("()") != 0:
    S = S.replace("()","")
    count += 1

print(count)