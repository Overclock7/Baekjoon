# https://www.acmicpc.net/problem/2693

T = int(input())
for i in range(T):
    lst = list(map(int,input().split()))
    lst.sort()
    print(lst[-3])