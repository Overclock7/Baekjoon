# https://www.acmicpc.net/problem/10988

noun = input()

if noun == noun[::-1]:
    print(1)
else :
    print(0)