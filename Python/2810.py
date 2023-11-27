# https://www.acmicpc.net/problem/2810

import sys
input = sys.stdin.readline

N = int(input())
seat = input().rstrip()

cup = (N+1) - seat.count('LL')

print(cup if cup <= N else N)