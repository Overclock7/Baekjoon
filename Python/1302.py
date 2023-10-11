# # https://www.acmicpc.net/problem/1302

lst = []
count = 0
favorite = []

for _ in range(int(input())):
    lst.append(input())

st = set(lst)

for s in st:
    if count < lst.count(s):
        count = lst.count(s)
        favorite.clear()
        favorite.append(s)
    elif count == lst.count(s):
        count = lst.count(s)
        favorite.append(s)
    else:
        pass

favorite.sort()

print(favorite[0])

# 2 (Overclock)

# import sys
# input = sys.stdin.readline

# dic = dict()

# for _ in range(int(input())):
#     s = input().rstrip()
#     if s not in dic.keys():
#         dic[s] = 1
#     else:
#         dic[s] += 1

# lst = sorted(dic.items(),key=lambda x:(-x[1],x[0]))

# print(lst[0][0])

# 3 (baekjoon)

# N = int(input())
# MP = {}

# for _ in range(N):
#     name = input().strip()

#     if name not in MP:
#         MP[name] = 0


#     MP[name] += 1

# print(sorted(MP.items(), key=lambda v: (-v[1], v[0]))[0][0])