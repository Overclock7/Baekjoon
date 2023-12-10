# https://www.acmicpc.net/problem/11501

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    S = list(map(int,input().split()))
    
    max = 0
    result = 0
    for stock in S[::-1]: # 뒤에서 부터 본다.
        if max < stock:
            max = stock
        else:
            result += max - stock

    print(result)