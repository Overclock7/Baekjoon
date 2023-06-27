
#테스트 횟수 입력
T = int(input())
for i in range(T):
    # 거스름돈 입력
    C = int(input())  
    temp = C
    # 코인 갯수 출력
    for i in [25,10,5,1]:
        output = temp // i
        print(output,end=" ")
        temp = temp % i
    print("")
