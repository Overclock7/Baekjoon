# https://www.acmicpc.net/problem/2903

# 초기값 지정
N = int(input())
init = 4
plus = 5
#알고리즘
for i in range(0,N):
    for j in range(2**i):
        init += plus
        plus += 2
#출력
print(init)