
import math

T = int(input())

for i in range(T):
    H,W,N = map(int, input().split())
    
    if N%H == 0:
        floor = H
    else:
        floor = N%H
    
    if N/H == W:
        room = W
    else:
        room = math.ceil(N/H)
        
    print("%d%02d"%(floor,room))