# https://www.acmicpc.net/problem/1316

n = int(input())
count = n

#1
for i in range(n):
    s = input()
    for j in range(len(s)-1):
        if s[j] == s[j+1]:  # 지금 글자와 다음 글자가 같으면 pass
            pass
        elif s[j] in s[j+1:]:   # 지금 글자와 다음 글자가 같지 않고,
            count -= 1          # 지금 글자가 다음 글자 이후로 존재하면,
            break

print(count)

#2 (baekjoon)

# s = 0

# for i in range(int(input())):
#     w = input()
#     l = list(set(w))
#     s += 1
#     for j in l:
#         if w.count(j*w.count(j))  == 1:
#             continue
#         else :
#             s -= 1
#             break

# print(s)