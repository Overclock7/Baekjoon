# https://www.acmicpc.net/problem/2798

N, M = map(int,input().split())
card = list(map(int,input().split()))
result = 0

for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if card[i]+card[j]+card[k] > result and card[i]+card[j]+card[k] <= M:
                result = card[i]+card[j]+card[k]
                
print(result)