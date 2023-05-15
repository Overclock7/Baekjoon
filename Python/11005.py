N , B = map(int,input().split())
temp = list()
num_list = list()

# B진수 숫자 구하기 위해 N을 B로 나누고, 나머지 구하기 진행
while True:
    if N > 0 :
        mod = N % B
        temp.append(mod)
        N = int(N / B)
    else :
        break

# 나머지 뒤집음 (B진수 순서에 맞게)
temp = temp[::-1]

# 10이 넘어가면 문자로 표시하기 위해 변환
for i in temp:
    if int(i) >= 10:
        num_list.append(chr(int(i)-10+ord('A')))
    else:
        num_list.append(str(int(i)))

# 리스트 --> String으로 변환
number = "".join(num_list)

print(number)