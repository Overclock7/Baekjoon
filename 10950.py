n = int(input())
a = list()
b = list()

for i in range(0,n):
    j,k = map(int,input().split())

    a.append(j)
    b.append(k)

for i in range(0,n):
    print(a[i]+b[i])