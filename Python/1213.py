# https://www.acmicpc.net/problem/1213

import sys
input = sys.stdin.readline

name = list(input().rstrip())
alpha = sorted(list(set(name)))
count = [0] * 26

for n in alpha:
    count[ord(n)-65] = name.count(n)

odd = 0
mid = ''
front = '' # rear는 front[::-1]
for n in alpha:
    if count[ord(n)-65] % 2 == 1:
        odd += 1
        mid = n
        if odd > 1:
            print("I'm Sorry Hansoo")
            exit(0)
    front += n * (count[ord(n)-65] // 2)

print(front+mid+front[::-1])

