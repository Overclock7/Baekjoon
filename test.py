import sys

n, x = map(int, sys.stdin.readline().split())

total = [1] + [0 for i in range(50)]
patty = [1] + [0 for i in range(50)]

for i in range(1, n + 1):
    patty[i] = patty[i - 1] * 2 + 1
    total[i] = total[i - 1] * 2 + 3


def dfs(n, x):
    half = (total[n] + 1) / 2
    if n == 1:
        if x == 0 or x == 1:
            return 0
        elif x == 2:
            return 1
        elif x == 3:
            return 2
        else:
            return 3
    if x == 1:
        return 0
    elif x == half - 1:
        return patty[n - 1]
    elif x == half:
        return patty[n - 1] + 1
    elif x > half:
        return patty[n - 1] + 1 + dfs(n - 1, x - half)
    else:
        return dfs(n - 1, x - 1)


print(dfs(n, x))
