# https://www.acmicpc.net/problem/10807

n = int(input())

l = list(map(int,input().split()))

look = int(input())

count = 0

for i in range(0,n):
    if l[i]==look :
        count += 1

print(count)