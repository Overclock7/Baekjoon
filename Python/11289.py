# https://www.acmicpc.net/problem/11289

import sys
input = sys.stdin.readline

for _ in range(int(input().strip())):
    S = [x for x in input().split()]
    stack = []

    for t in S[1:]:
        if t.isalpha():
            if t == "A":
                b = stack.pop()
                a = stack.pop()
                stack.append(a and b)
            elif t == "R":
                b = stack.pop()
                a = stack.pop()
                stack.append(a or b)
            elif t == "X":
                b = stack.pop()
                a = stack.pop()
                result = stack.append(((not a) and b) or (a * (not b)))
            elif t == "N":
                a = stack.pop()
                result = stack.append(not a)
        else:
            stack.append(int(t))
    
    print(int(stack.pop()))