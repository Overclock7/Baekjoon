# https://www.acmicpc.net/problem/9063

N = int(input())
x_list = list()
y_list = list()

for i in range(N):
    x, y = map(int,input().split())
    x_list.append(x)
    y_list.append(y)

x_list.sort()
y_list.sort()

W = x_list[-1] - x_list[0]
H = y_list[-1] - y_list[0]
print(W*H)

