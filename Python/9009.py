# https://www.acmicpc.net/problem/9009

import sys
input = sys.stdin.readline

# 피보나치 수열 생성
fibo = [0] * 46
fibo[0] = 0
fibo[1] = 1
for i in range(2,46):
    fibo[i] = fibo[i-1] + fibo[i-2]

T = int(input())
for _ in range(T):
    N = int(input())
    
    answer =[]
    for i in range(45,0,-1):
        if fibo[i] <= N:
            N -= fibo[i]
            answer.append(fibo[i])
        
        if N == 0:
            answer.sort()
            print(" ".join(map(str,answer)))
            break