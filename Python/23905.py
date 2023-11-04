# https://www.acmicpc.net/problem/23905

import sys

input = sys.stdin.readline

T = int(input())
for t in range(T):
    N , K = map(int,input().rstrip().split())
    lst = list(map(int,input().rstrip().split()))
    result = 0
    countdown = K

    for i in range(N):
        if lst[i] != countdown: # 값이 안맞으면 countdown 초기화
            countdown = K
        if lst[i] == countdown: # 값이 맞으면 countdown 수 하나씩 줄임
            countdown -= 1
            if countdown == 0: # countdown == 0 이 되면 countdown 하나 찾음
                result += 1
                countdown = K

    print(f"Case #{t+1}: {result}")