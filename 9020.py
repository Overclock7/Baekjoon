
T = int(input())

#소수 리스트 생성
li = [True] * 10001
li[0] = li[1] = False 

for i in range(2,10001):
    if li[i] == True:
        for j in range(i+i,10001,i):
            li[j] = False

#찾기 시작
for _ in range(T):
    n = int(input())
    a = b = int(n / 2)
    while not(a <= 0) :
        # 둘 다 소수이면
        if li[a] & li[b]:
            print(a,b)
            break # while문 탈출
        else:
            a -= 1
            b += 1