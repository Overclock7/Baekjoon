# https://www.acmicpc.net/problem/1427

import sys

num_list = list(input())

num_list.sort(reverse=True)

print("".join(num_list))