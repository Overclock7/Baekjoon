
import math

A,B,V = map(int,input().split())

div = math.ceil((V - A) / (A - B)) + 1

print(div)