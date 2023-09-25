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

# Baekjoon

# import sys
# from collections import deque

# N = int(sys.stdin.readline())
# queue = deque()
# for _ in range(N):
#     cmd = sys.stdin.readline().split()
#     if cmd[0] == 'push':
#         queue.append(cmd[1])


#     elif cmd[0] == 'pop':
#         if queue:
#             print(queue.popleft())
#         else:
#             print(-1)

#     elif cmd[0] == 'size':
#         print(len(queue))

#     elif cmd[0] == 'empty':
#         print(0) if queue else print(1)

#     elif cmd[0] == 'front':
#         print(queue[0]) if queue else print(-1)

#     elif cmd[0] == 'back':
#         print(queue[-1]) if queue else print(-1)