# https://www.acmicpc.net/problem/17829

import sys

input = sys.stdin.readline

def pooling_222(matrix, n):
    
    if n == 1: # 1 x 1 matrix 남은 상태
        return matrix[0][0]
        
    new_matrix = [[] for _ in range(n//2)]
    for i in range(0,n,2): # 2칸씩 뛰어 넘음
        for j in range(0,n,2): # 2칸씩 뛰어 넘음
            new_matrix[i//2].append(sorted([matrix[i][j],matrix[i][j+1],matrix[i+1][j],matrix[i+1][j+1]])[2])
    
    return pooling_222(new_matrix,n//2)
    
N = int(input())
matrix = list(list(map(int,input().split())) for _ in range(N))
print(pooling_222(matrix,N))
