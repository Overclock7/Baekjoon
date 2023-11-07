# https://www.acmicpc.net/problem/10830

import sys

input = sys.stdin.readline

def make_idenity_matrix(n):
    identity_matrix = list(list(0 for _ in range(n)) for _ in range(n))
    for i in range(n):
        for j in range(n):
            if i == j:
                identity_matrix[i][j] = 1
                                
    return identity_matrix

def product_matrix(x,y,n,modulo):
    result = list(list(0 for _ in range(n)) for _ in range(n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += x[i][k] * y[k][j]
            result[i][j] %= modulo
    return result

def power_matrix(matrix,exp,n,modulo):
    
    matrix_1 = product_matrix(matrix,make_idenity_matrix(n),n,modulo)
    if exp == 1:
        return matrix_1
    
    matrix_2 = power_matrix(matrix,exp//2,n,modulo)
    if exp % 2 == 1:
        return product_matrix(product_matrix(matrix_2,matrix_2,n,modulo),matrix_1,n,modulo)
    else:
        return product_matrix(matrix_2,matrix_2,n,modulo)
    
N, B = map(int,input().split())
matrix = list(list(map(int,input().split())) for _ in range(N))
result = power_matrix(matrix,B,N,1000)
for i in range(N):
    for j in range(N):
        print(result[i][j], end =" ")
    print()