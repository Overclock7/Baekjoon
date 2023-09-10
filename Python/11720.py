# https://www.acmicpc.net/problem/11720

n = int(input())

# 1
n_list = list(str(input()))

sum = 0

for i in range(0,n): 
    sum += int(n_list[i])

print(sum)

# 2 (baekjoon)
# n_list = sum(map(int,input()))
# print(n_list)