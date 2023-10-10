# https://www.acmicpc.net/problem/13237

import sys
input = sys.stdin.readline

tree = dict()

T = int(input())

for data in range(1,T+1):
    parent = int(input())
    tree[data] = parent

for data,parent in tree.items():
    height = 0
    while parent != -1:
        height += 1
        parent = tree[parent]
    print(height)

# 2 (Overclock0708)

# class Node:
#     def __init__(self,data = None,parent = None) :
#         self.data = data
#         self.parent = parent
#         self.height = None
#     def __str__(self):
#         return self.data.__str__()

# T = int(input())

# lst = []
# lst.append(Node())

# for i in range(1,T+1):
#     lst.append(Node(i,int(input())))

# for node in lst[1:] :
#     height = 0
#     if node.parent == -1:
#         node.height = height
#     else:
#         height = 1
#         loc = node.parent
#         while lst[loc].parent != -1:
#             height += 1
#             loc = lst[loc].parent
#         node.height = height

# for i in lst[1:]:
#     print(i.height)
