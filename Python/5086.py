# https://www.acmicpc.net/problem/5086

while True:
    try: 
        A,B = map(int,input().split())

        if A <= B : # 첫 번째 숫자가 두번째 숫자의 약수인가?
            if B % A == 0:
                print("factor")
            else :
                print("neither")       
        elif A > B :
            if A % B == 0:
                print("multiple")
            else :
                print("neither")
    except:
        break
