# https://www.acmicpc.net/problem/1157


s = input().upper()
l1 = list()
l2 = list()

#알파벳 갯수 세기
for i in range(ord("A"),ord("Z")+1):
    l1.append(s.count(chr(i)))

# 갯수 중 가장 큰 수
max = max(l1)

# 가장 큰 수의 index를 l2에 넣기
for i in range(len(l1)):
    if l1[i] == max :
        l2.append(i)

# 조건에 맞게 출력
if len(l2) == 1 :
    ascii_code=ord('A')+l2[0]
    print(chr(ascii_code))
else :
    print("?")
