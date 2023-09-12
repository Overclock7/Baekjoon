# https://www.acmicpc.net/submit/10989

import sys

num_list = [0] * 10001
for n in range(int(sys.stdin.readline())):
    num_list[int(sys.stdin.readline())] += 1

for i in range(len(num_list)):
    if num_list[i] != 0:
        temp = num_list[i]
        for j in range(temp):
            print(i)