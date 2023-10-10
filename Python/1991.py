# https://www.acmicpc.net/problem/1991

def preorder(node):
    if node != '.':
        print(node,end="")
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if node != '.':
        inorder(tree[node][0])
        print(node,end="")
        inorder(tree[node][1])
        
def postorder(node):
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node,end="")

tree = {}
for i in range(int(input())):
    data,L,R = map(str,input().split())
    tree[data] = [L,R]

preorder('A')
print()
inorder('A')
print()
postorder('A')

# 2 (Overclock0708)

# import sys
# input = sys.stdin.readline

# class Node():
#     def __init__(self,D,L,R):
#         self.D = D
#         self.L = L
#         self.R = R

# def inorder(root):
#     if root != '.':
#         inorder(tree[root].L)
#         print(tree[root].D,end="")
#         inorder(tree[root].R)

# def preorder(root):
#     if root != '.':
#         print(tree[root].D,end="")
#         preorder(tree[root].L)
#         preorder(tree[root].R)

# def postorder(root):
#     if root != '.':
#         postorder(tree[root].L)
#         postorder(tree[root].R)
#         print(tree[root].D,end="")

# tree = dict()

# for _ in range(int(input())):
#     D,L,R = input().rstrip().split()
#     node = Node(D,L,R)
#     tree[D] = node

# preorder('A')
# print("")
# inorder('A')
# print("")
# postorder('A')