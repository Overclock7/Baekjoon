# https://www.acmicpc.net/problem/15312

import sys
input = sys.stdin.readline

alpha = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

name_1 = input().rstrip()
name_2 = input().rstrip()

lst = []

for i, j in zip(name_1,name_2):
    lst.append(alpha[ord(i)-65])
    lst.append(alpha[ord(j)-65])

while len(lst) > 2:
    temp = []
    for i in range(1,len(lst)):
        temp.append((lst[i-1]+lst[i]) % 10)
    lst = temp.copy()
    
print("%d%d"%(lst[0],lst[1]))