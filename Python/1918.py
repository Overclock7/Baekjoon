# https://www.acmicpc.net/problem/1918

import sys

infix = sys.stdin.readline().strip()
stack = []
postfix = ""

for t in infix:
    if t.isalpha():
        postfix += t
        
    else:
        if t == "(":
            stack.append(t)

        elif t == '*' or t == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                postfix += stack.pop()
            stack.append(t)

        elif t == '+' or t == '-':
            while stack and (stack[-1] != '('):
                postfix += stack.pop()
            stack.append(t)

        elif t == ')':
            while stack and (stack[-1] != "("):
                postfix += stack.pop()
            stack.pop()

while stack:
    postfix += stack.pop()

print(postfix)



