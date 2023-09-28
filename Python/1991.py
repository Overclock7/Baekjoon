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