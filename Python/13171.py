# https://www.acmicpc.net/problem/13171

import sys

input = sys.stdin.readline

def power_modulo(base,exp,modulo):
    
    base_1 = base % modulo
    if exp == 1:
        return base_1
    if exp == 0:
        return 1

    base_2 = power_modulo(base,exp//2,modulo)
    if exp % 2 == 0:
        return ( base_2 * base_2 ) % modulo
    else:
        return ( ( base_2 * base_2 ) * (base_1) ) % modulo


A = int(input())
X = int(input())
print(power_modulo(A,X,1000000007))
