n = int(input())

l = []

for i in range(0,n):
    l.append(str(input()))

for i in range(0,n):
    print(l[i][0]+l[i][-1])