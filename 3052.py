import sys

n = 10
l = list()
count = 1

for i in range(0,n):
    l.append(int(sys.stdin.readline())%42)

l.sort()

for i in range(0,n-1):
    if(l[i]!=l[i+1]):
        count += 1

print(count)