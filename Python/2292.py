# https://www.acmicpc.net/problem/2292

standard = 1
num = int(input())
mul = 0

while True:
    standard += mul * 6
    if standard >= num:
        print(mul+1)
        break
    mul += 1
    