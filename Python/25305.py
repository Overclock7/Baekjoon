# https://www.acmicpc.net/problem/25305

N , k = map(int,input().split())
scores = list(map(int,input().split()))
scores.sort()
print(scores[N-k])