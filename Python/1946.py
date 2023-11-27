# https://www.acmicpc.net/problem/1946

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    R = [0]*(N+1)
    for i in range(N):
        paper, interview = map(int,input().split())
        R[paper] = interview
    
    result = 1 # 서류심사 1등은 무조건 선발
    top = R[1] # 1등의 면접심사 등수
    for i in range(2,N+1):
        if R[i] < top:
            top = R[i]
            result += 1
            
    print(result)
    
# 2 (overclock0708)

# import sys
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     N = int(input())
#     #서류면접 순위로 정렬
#     R = sorted([list(map(int,input().split())) for _ in range(N)])
    
#     result = 1 # 서류면접 1등은 무조건 선발
#     top = R[0][1]
#     for i in range(1,N):
#         if R[i][1] < top:
#             top = R[i][1]
#             result += 1
    
#     print(result)