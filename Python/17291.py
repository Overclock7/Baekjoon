# https://www.acmicpc.net/problem/17291

import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 21
# dp : 년도 말 개체수
dp[0] = dp[1] = 1

# i는 년도
for i in range(2,N+1):
    # i년 1월에 하는 것 (Birth)
    dp[i] = dp[i-1] * 2
    
    # i년 2월에 하는 것 (Death)
    if ((i - 3) > 0) and ((i - 3) % 2 == 1):
        dp[i] -= dp[i-4]
    if ((i - 4) > 0) and ((i - 4) % 2 == 0):
        dp[i] -= dp[i-5]
        
print(dp[N])