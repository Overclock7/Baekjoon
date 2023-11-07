# https://www.acmicpc.net/problem/11582

import sys

input = sys.stdin.readline

def chicken_top_n(lst,n,k):
    sort_lst = list()
    step = n // k
    for i in range(0,N,step):
        sort_lst += sorted(lst[i:i+step])
    return sort_lst


N = int(input())
lst = list(map(int,input().rstrip().split()))
K = int(input())
print(*(chicken_top_n(lst,N,K)))