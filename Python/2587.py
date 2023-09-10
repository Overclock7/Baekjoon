# https://www.acmicpc.net/problem/2587

n_list = list(map(int,(input() for i in range(5))))

print(sum(n_list)//5)
print(sorted(n_list)[2])