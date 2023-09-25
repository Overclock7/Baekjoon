# https://www.acmicpc.net/problem/18258

import sys

q = []
index = 0

for i in range(int(sys.stdin.readline())):
    S = sys.stdin.readline().strip().split()
    if S[0] == 'push':
        q.append(int(S[1]))
    elif S[0] == 'pop':
        if len(q) - index > 0:
            print(q[index])
            index += 1
        else:
            print(-1)
    elif S[0] == 'size':
        print(len(q) - index)
    elif S[0] == 'empty':
        if len(q) - index > 0:
            print(0)
        else:
            print(1)
    elif S[0] == 'front':
        if len(q) - index > 0:
            print(q[index])
        else:
            print(-1)
    elif S[0] == 'back':
        if len(q) - index > 0:
            print(q[-1])
        else:
            print(-1)
