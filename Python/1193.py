# https://www.acmicpc.net/problem/1193


line = 1
n = int(input())

while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    print(f"{n}/{line-n+1}")
else:
    print(f"{line-n+1}/{n}")