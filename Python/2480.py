# https://www.acmicpc.net/problem/2480

A,B,C = map(int,input().split())

money = 0

if (A==B==C):
    money = 10000+A*1000
elif (A==B or B==C or C==A):
    if(A==B):
        money = 1000+A*100
    if(B==C):
        money = 1000+B*100
    if(C==A):
        money = 1000+C*100
else:
    money = max(A,B,C)*100

print(money)    