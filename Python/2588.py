# https://www.acmicpc.net/problem/2588

A = int(input())
B = list(input())

B_2 = int(B[0])
B_1 = int(B[1])
B_0 = int(B[2])

print(A*B_0)
print(A*B_1)
print(A*B_2)
print(100*A*B_2+10*A*B_1+1*A*B_0)