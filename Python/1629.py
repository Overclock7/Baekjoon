# https://www.acmicpc.net/problem/1629

import sys

input = sys.stdin.readline

# 거듭제곱 계산기
def power_modulo(base,exp,modulo):
    
    if exp == 1:
        return base % modulo
    if exp == 0:
        return 1

    base_1 = base % modulo
    base_2 = power_modulo(base,exp//2,modulo)
    if exp % 2 == 0: # 제곱 수가 짝수이면
        return ( base_2 * base_2 ) % modulo
    else: # 제곱 수가 홀수 이면
        return ( ( base_2 * base_2 ) * (base_1) ) % modulo


A, B, C = map(int,input().split())
print(power_modulo(A,B,C))
