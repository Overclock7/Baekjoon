# https://www.acmicpc.net/problem/10214

N = int(input())

for i in range(N):
    yonsei, korea = 0, 0
    for j in range(9):
        x, y = map(int,input().split())
        yonsei += x
        korea += y
    if yonsei > korea:
        print('Yonsei')
    elif yonsei < korea:
        print('Korea')
    else:
        print('Draw')