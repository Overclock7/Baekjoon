# https://www.acmicpc.net/problem/1463

import sys

n = int(input())
lst = [0] * (n+1)

for i in range(2,n+1):
    lst[i] = lst[i-1] + 1 # 초기값 설정
    if i % 2 == 0:
        lst[i] = min(lst[i//2] + 1, lst[i]) # i 가 만약 2의 배수였다면
    if i % 3 == 0:
        lst[i] = min(lst[i//3] + 1, lst[i]) # i 가 만약 3의 배수였다면

print(lst[n])