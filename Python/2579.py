# https://www.acmicpc.net/problem/2579

import sys

n = int(input())
step = [0] + [int(input()) for i in range(n)]
lst = [0] * (n+1)

while True:
    if n <= 2:
        print(sum(step))
        break
        
    lst[1] = step[1]
    lst[2] = step[1] + step[2]
    
    for i in range(3,n+1):
        lst[i] = max(lst[i-2],lst[i-3]+step[i-1]) + step[i]
    
    print(lst[n])
    break