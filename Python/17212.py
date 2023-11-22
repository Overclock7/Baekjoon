# https://www.acmicpc.net/problem/17212

import sys
input = sys.stdin.readline

N = int(input())
coin = [0] * 100001

coin[1] = coin[2] = coin[5] = coin[7] = 1
coin[3] = coin[4] = coin[6] = 2

for i in range(8,N+1):
    coin[i] = min(coin[i-1],coin[i-2],coin[i-5],coin[i-7]) + 1
    
print(coin[N])