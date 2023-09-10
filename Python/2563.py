# https://www.acmicpc.net/problem/2563

paper = [[0]*100 for i in range(100)]
count = 0

for i in range(int(input())):
    a, b = map(int,input().split())
    a -= 1
    b -= 1
    for j in range(a,a+10):
        for k in range(b,b+10):
            paper[j][k] = 1

for i in range(100):
    count += paper[i].count(1)

print(count)