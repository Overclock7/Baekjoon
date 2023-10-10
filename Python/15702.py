# https://www.acmicpc.net/problem/15702

import sys
input = sys.stdin.readline

N , M = map(int,input().split())

score = list(map(int,input().split()))
lst_result = list()

for _ in range(M):
    lst = list(input().split())
    idx = lst[0]
    chk = lst[1:]

    result = 0
    for c,s in zip(chk,score): # zip 함수 활용
        if c == 'O':
            result += s
    
    lst_result.append((idx,result))

lst_result.sort(key=lambda x:(-x[1],x[0]))

print(lst_result[0][0],lst_result[0][1])