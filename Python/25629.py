import math

N = int(input())
num = list(map(int,input().split()))
odd, even = 0 , 0

for i in num :
    if i % 2 == 1:
        odd += 1
    else:
        even += 1

if odd == math.ceil(N / 2)  and even == N // 2 :
    # math.ceil() : 올림
    print(1)
else :
    print(0)