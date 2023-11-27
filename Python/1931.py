# https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

N = int(input())
R = [[0] * 2 for _ in range(N)]
for i in range(N):
    start, end = map(int,input().split())
    R[i][0] = start
    R[i][1] = end

R.sort(key = lambda x:(x[1],x[0])) # 1) 빨리 끝나는 순 2) 빨리 시작하는 순

time = 0 # 끝 시간을 저장함.
result = 0
for r in R:
    if time <= r[0]:
        time = r[1]
        result += 1

print(result)