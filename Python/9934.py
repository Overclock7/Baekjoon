# https://www.acmicpc.net/problem/9934

import sys
input = sys.stdin.readline

def inorder(lst,depth):
    mid = len(lst) // 2
    level[depth].append(lst[mid])
    if len(lst) == 1:
        return
    inorder(lst[:mid],depth+1)
    inorder(lst[mid+1:],depth+1)

K = int(input())
lst = list(map(int,input().rstrip().split()))
level = [[] for _ in range(K)] # level을 위한 2차원 배열

inorder(lst,0)
for i in level:
    print(*i) # 리스트 출력