# https://www.acmicpc.net/problem/2566

l = [list(map(int,input().split())) for _ in range(9)]

max = -1
loc_row = 0
loc_col = 0

for i in range(9):
    for j in range(9):
        if max < l[i][j]:
            max = l[i][j]
            loc_row = i + 1
            loc_col = j + 1


print(max)
print(loc_row,loc_col)