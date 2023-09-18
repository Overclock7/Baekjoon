# https://www.acmicpc.net/problem/11478

S = input()

list_S = []

for i in range(len(S)):
    for j in range(i+1,len(S)+1):
        list_S.append(S[i:j])

set_S = set(list_S)

print(len(set_S))