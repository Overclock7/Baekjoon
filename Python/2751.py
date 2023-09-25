# https://www.acmicpc.net/problem/2751

import sys

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for i in range(N)]
nums.sort()
for n in nums:
    print(n)

# Overclock0708

# def mergeSort(x):
#     if len(x) > 1:
#         mid = len(x) // 2
#         left, right = x[:mid], x[mid:]
#         mergeSort(left)
#         mergeSort(right)

#         index_left, index_right, index_x = 0 ,0, 0

#         while index_left < len(left) and index_right < len(right):
#             if left[index_left] < right[index_right]:
#                 x[index_x] = left[index_left]
#                 index_left += 1
#             else:
#                 x[index_x] = right[index_right]
#                 index_right += 1
#             index_x += 1

#         while index_left < len(left):
#             x[index_x] = left[index_left]
#             index_left += 1
#             index_x += 1
#         while index_right < len(right):
#             x[index_x] = right[index_right]
#             index_right += 1
#             index_x += 1

#         return x
