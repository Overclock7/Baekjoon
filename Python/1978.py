
n = int(input())
li = list(map(int,input().split()))
li2 = []
count = 0

for i in li:
    if i == 1:
        continue
    else:
        for j in range(1,i+1):
            if i % j == 0:
                li2.append(i)

        if len(li2) == 2:
            count += 1

        li2 = []

print(count)