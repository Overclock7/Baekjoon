# https://www.acmicpc.net/problem/2810

import sys
input = sys.stdin.readline

N = int(input())
seat = input().rstrip()

# 싱글석만 있을 경우의컵 수는 관객수 + 1 인데 커플석 사이엔 컵이 없다.
cup = (N+1) - seat.count('LL')

print(cup if cup <= N else N) # 싱글석만 있을 경우엔 관객 수만큼만 출력