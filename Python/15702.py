# https://www.acmicpc.net/problem/15702

N, M = map(int,input().split())

score = list(map(int,input().split()))
dic = dict()

for _ in range(M):
    paper = list(input().split())
    temp = 0
    for i in range(N):
        if paper[i+1] == 'O':
            temp += score[i]
    dic[int(paper[0])] = temp

sort_dic = sorted(dic.items(),key=lambda x:(-x[1],x[0]))

print(sort_dic[0][0],sort_dic[0][1])