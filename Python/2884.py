# https://www.acmicpc.net/problem/2884

H , M = map(int,input().split())

if (M-45<0):
    H = H-1
    M = M+60
    
    if(H<0):
        H=23

print(H, M-45)