n = int(input())

for i in range(1,n+1) :
    print(' '*(n-i),'*'*(i*2-1),sep='')

for i in range(1,n):
    print(' '*i,'*'*(2*n-(2*i+1)),sep='')