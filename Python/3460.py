# https://www.acmicpc.net/problem/3460

T = int(input())

for i in range(T):
    N = int(input())
    # '0b' 문자열 제거 및 비트 배열 뒤집기
    binary_N_reverse = bin(N)[:1:-1]
    for j in range(len(binary_N_reverse)):
        if binary_N_reverse[j] == '1':
            print(j,end=" ")