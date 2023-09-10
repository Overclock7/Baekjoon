# https://www.acmicpc.net/problem/8958

import sys

n = int(input())
for i in range(0,n):
    ox_list = list(sys.stdin.readline())
    score = 0
    total_score = 0
    
    for result in ox_list:
        if result == "O":
            score += 1
            total_score += score
        else:
            score = 0
    print(total_score)