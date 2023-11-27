# https://www.acmicpc.net/problem/5585

import sys
input = sys.stdin.readline

coin_lst = [500,100,50,10,5,1]

N = int(input())
coin = 1000 - N

result = 0
for c in coin_lst:
    result += coin // c
    coin = coin % c
    if coin == 0:
        break

print(result)