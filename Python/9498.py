# https://www.acmicpc.net/problem/9498

score = int(input())

if(score<60):
    print("F")
elif(score<70):
    print("D")
elif(score<80):
    print("C")
elif(score<90):
    print("B")
elif(score<101):
    print("A")