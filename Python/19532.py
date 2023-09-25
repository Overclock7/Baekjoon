# https://www.acmicpc.net/problem/19532

a,b,c,d,e,f = map(int,input().split())

for x in range(-999,1000):
    for y in range(-999,1000):
        if a*x+b*y == c and d*x+e*y == f:
            print(x,y)

# Overclock0708 (Use Numpy)

# import numpy as np

# a,b,c,d,e,f = map(int,input().split())

# Cremer's rule 사용

# g = np.array([[c,b],[f,e]])
# h = np.array([[a,c],[d,f]])
# i = np.array([[a,b],[d,e]])

# x = int(np.linalg.det(g) / np.linalg.det(i))
# y = int(np.linalg.det(h) / np.linalg.det(i))

# print(x, y)