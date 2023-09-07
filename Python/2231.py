N = int(input())
result = 0

for i in range(0,N):
    num_sum = sum(list(map(int,str(i))))
    if i + num_sum == N:
        result = i
        break

print(result)