# https://www.acmicpc.net/problem/1427

import sys
input = sys.stdin.readline

# 중요
# .sort()는 리스트에서만...
print("".join(sorted(input().strip(),reverse=True)))

# 2 (Overclock0708)

# num_list = list(input())

# num_list.sort(reverse=True)

# print("".join(num_list))
