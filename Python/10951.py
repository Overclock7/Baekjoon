import sys

while(True):
    try:
        a,b = map(int,sys.stdin.readline().split())
        if((a>0 and a<10) and (b>0 and b<10)):
            print(a+b)
    except:
        break