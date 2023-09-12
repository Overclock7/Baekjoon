# https://www.acmicpc.net/problem/11098

for _ in range(int(input())):
    lst = []
    for _ in range(int(input())):
        cost, name = map(str,input().split())
        lst.append([int(cost), name])
    lst.sort(key = lambda x:x[0],reverse=True)
    print(lst[0][1])