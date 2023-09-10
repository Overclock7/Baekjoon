# https://www.acmicpc.net/problem/5622

s = input()
count = 0

for i in s:
    
    k = ord(i)

    if k <= ord("C"):
        count +=3
    elif k <= ord("F"):
        count +=4
    elif k <= ord("I"):
        count +=5
    elif k <= ord("L"):
        count +=6
    elif k <= ord("O"):
        count +=7
    elif k <= ord("S"):
        count +=8
    elif k <= ord("V"):
        count +=9
    elif k <= ord("Z"):
        count +=10

print(count)