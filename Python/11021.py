import sys

n = int(sys.stdin.readline())

for i in range(0,n):
    print(f"Case #{i+1}: {sum(map(int,sys.stdin.readline().split()))}")