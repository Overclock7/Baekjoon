# https://www.acmicpc.net/problem/2581

M = int(input())
N = int(input())

temp = []
li = []
count = 0

for i in range(M,N+1):
    if i == 1:
        continue
    else:
        for j in range(1,i+1):
            if i % j == 0:
                temp.append(i)

        if len(temp) == 2:
            count += 1
            li.append(i)
            
        temp = []

if count == 0:
    print(-1)
else:
    print(sum(li))
    print(li[0])