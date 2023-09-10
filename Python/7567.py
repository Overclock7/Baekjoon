# https://www.acmicpc.net/problem/7567

bowl = input()
result = 0
temp = None
for i in bowl:
    if temp == i:
        result += 5
    elif temp != i :
        result += 10
        temp = i
print(result)