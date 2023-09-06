a1 , a0 = map(int,input().split())
c = int(input())
n0 = int(input())
result = 1

for i in range(n0,101):
    f = a1 * i + a0
    g = c * i
    if f > g:
        result = 0

print(result)
