N = int(input())
count = 0
num = 0

while True:
    num += 1
    str_num = str(num)
    check = str_num.find("666")
    if check == -1:
        continue
    else:
        count += 1
        if count == N:
            break

print(num)
