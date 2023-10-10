# https://www.acmicpc.net/problem/11720

n = int(input())

n_list = list(str(input()))

sum = 0

for i in range(0,n): 
    sum += int(n_list[i])

print(sum)

# 2 (Baekjoon)

# n = int(input())
# n_list = sum(map(int,input()))
# print(n_list)