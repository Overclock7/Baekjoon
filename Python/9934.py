# https://www.acmicpc.net/problem/9934

def inorder(lst,depth):
    mid = len(lst) // 2
    array[depth].append(lst[mid])
    if len(lst) == 1:
        return
    inorder(lst[:mid],depth+1)
    inorder(lst[mid+1:],depth+1)


K = int(input())
lst = list(map(int,input().split()))
array = [[] for _ in range(K)]

inorder(lst,0)
for i in array:
    print(*i)