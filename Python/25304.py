total = int(input())
num = int(input())

check = 0
a = list()
b = list()

for i in range(0,num):
    c,d=map(int,input().split())
    a.append(c)
    b.append(d)
    check += a[i]*b[i]

if(check==total):
    print("Yes")
else:
    print("No")
    