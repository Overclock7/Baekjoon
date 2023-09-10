# https://www.acmicpc.net/problem/10951

import sys

while(True):
    try:
        a,b = map(int,sys.stdin.readline().split())
        if((a>0 and a<10) and (b>0 and b<10)):
            print(a+b)
    except:
        break