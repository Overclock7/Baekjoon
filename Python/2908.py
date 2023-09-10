# https://www.acmicpc.net/problem/2908

n1,n2 = input().split()

#1
r1 = int(n1[::-1]) #[::-1] 역순
r2 = int(n2[::-1])

print(max(r1,r2))

#2(Baekjoon)
r1 = int(''.join(reversed(n1)))
r2 = int(''.join(reversed(n1)))

print(max(r1,r2))