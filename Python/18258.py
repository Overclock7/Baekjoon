# https://www.acmicpc.net/problem/18258

import sys
input = sys.stdin.readline

#Queue에서는 front,rear 선언해서 활용하자
queue = list()
front = 0
rear = 0
for _ in range(int(input())):
    ipt = list(input().rstrip().split())
    command = ipt[0]
    if command == 'push':
        queue.append(ipt[1])
        rear += 1
    elif command == 'pop':
        if front == rear:
            print(-1)
        else:
            print(queue[front])
            front += 1
    elif command == 'size':
        print(rear-front)
    elif command == 'empty':
        print(1 if front == rear else 0)
    elif command == 'front':
        print(-1 if front == rear else queue[front])
    elif command == 'back':
        print(-1 if front == rear else queue[rear-1])

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