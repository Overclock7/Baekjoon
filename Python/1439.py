# https://www.acmicpc.net/problem/1439

import sys
input = sys.stdin.readline

S = input().rstrip()

result = max(S.count('10'),S.count('01')) # 둘 중 큰 값이 답임

print(result)