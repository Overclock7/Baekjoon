# https://www.acmicpc.net/problem/18870

import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))

dic = dict()
for k,v in enumerate(sorted(list(set(lst)))):
    dic[v] = k

for i in lst:
    print(dic[i],end=" ")