# https://www.acmicpc.net/problem/1052

import sys
input = sys.stdin.readline

N, K = map(int,input().split())

result = 0
while bin(N).count('1') > K:
    index = bin(N)[::-1].index('1') # 가장 오른쪽 1의 위치 찾기
    result += 2 ** index
    N += 2 ** index

print(result)

# 2 (baekjoon)

# import sys
# input = sys.stdin.readline

# N, K = map(int,input().split())

# temp = N
# while bin(temp)[2:].count('1') > K:
#     temp += 1
# print(temp - N)