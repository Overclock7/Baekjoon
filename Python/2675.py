
n = int(input())

for i in range(n):
    num,string = input().split()
    for i in string:
        print(i*int(num),end="")
    print()