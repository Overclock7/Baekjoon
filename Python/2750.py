N = int(input())
n_list = list()

for i in range(N):
    n_list.append(int(input()))

# n_list.sort()

# bubble sort
for j in range(N-1,0,-1):
    for k in range(j):
        if n_list[k] > n_list[k+1]:
            n_list[k] , n_list[k+1] = n_list[k+1] , n_list[k]


for n in n_list:
    print(n)

