N = int(input())

count_3 = 0
count_5 = 0 # like flag

while True:
    if N < 0:
        count_5 = -1
        break
    elif N % 5 == 0:
        count_5 =  N //5
        break

    N = N - 3
    count_3 += 1

if count_5 == -1 :
    print(-1)
else:
    print(count_3 + count_5)