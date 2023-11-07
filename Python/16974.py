# https://www.acmicpc.net/problem/16974

import sys

input = sys.stdin.readline

n, x = map(int,input().rstrip().split())

burger = [1] + [0 for _ in range(50)]
patty = [1] + [0 for _ in range(50)]

for i in range(1,n+1):
    burger[i] = burger[i-1] * 2 + 3
    patty[i] = patty[i-1] * 2 + 1
    
def eat(n,x):
    if n == 0: # level-0 버거는 패티 밖에 없음
        return x
    if x == 1: # 처음
        return 0
    elif x <= burger[n-1] + 1: # 처음 이후 중간 패티 이전
        return eat(n-1,x-1)
    elif x == 1 + burger[n-1] + 1: # 중간 패티
        return patty[n-1] + 1
    elif x <= 1 + burger[n-1] + 1 + burger[n-1]: # 중간 패티 이후 마지막 이전
        return patty[n-1] + 1 + eat(n-1,x-(1+burger[n-1]+1))
    elif x == burger[n]: # 마지막
        return patty[n]
    
print(eat(n,x))