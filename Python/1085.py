# https://www.acmicpc.net/problem/1085

x,y,w,h = map(int,input().split())

list = [x-0,y-0,w-x,h-y]

print(min(list))