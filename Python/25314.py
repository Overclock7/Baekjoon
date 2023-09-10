# https://www.acmicpc.net/problem/25314

import math

N = int(input())

P = math.ceil(N/4)

for i in range(0,P):
    print("long",end=" ")

print("int")