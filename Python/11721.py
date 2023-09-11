# https://www.acmicpc.net/problem/11721

str_list = input()

for i in range(len(str_list)):
    if i == 0:
        pass
    elif i % 10 == 0:
        print("")
    print(str_list[i],end="")