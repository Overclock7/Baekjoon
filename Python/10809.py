# https://www.acmicpc.net/problem/10809

S = input()

for i in range(26):
    print(S.find(chr(97+i)),end=' ')


# Overclock0708

# s = input()
# list_s = list()
# location = 0

# # list 초기화
# for i in range(26):
#     list_s.append(-1)

# # 문자 판별
# for i in s:
#     k = ord(i) - 97
#     if(list_s[k]==-1):
#         list_s[k] = location
#     location += 1

# # 출력
# for i in list_s :
#     print(i,end=" ")
