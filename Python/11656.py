# https://www.acmicpc.net/problem/11656

s = input()
lst = []

for i in range(len(s)):
    lst.append(s[i:len(s)])

lst.sort()

for s in lst:
    print(s)