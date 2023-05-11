import sys

year = int(sys.stdin.readline())

if ((year%400 == 0)|((year%4==0)&(year%100 != 0))) :
    print("윤년입니다.")
else :
    print("윤년아님")
