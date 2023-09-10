# https://www.acmicpc.net/problem/11170

T = int(input())
for i in range(T):
    N , M = map(int,input().split())
    result = ''.join(str(i) for i in range(N,M+1))
    print(result.count('0'))

