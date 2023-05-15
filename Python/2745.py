
N,B = map(str,input().split(" "))
B = int(B)

temp = list()
total = 0
order = 0

# 각 자리 문자 --> 숫자
for i in N:
    if ord(i) in range(ord("A"),ord("Z")+1) :
        temp.append(ord(i) - ord("A") + 10)
    elif int(i) in range(0,10):
        temp.append(int(i))

#길이 구하기
order = len(temp)

# 합 구하기
for i in temp :
    order -= 1
    total += i * B**order

print(total)
