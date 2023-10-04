# https://www.acmicpc.net/problem/6996

for i in range(int(input())):
    A , B = input().split()
    lst_A = list(A)
    lst_B = list(B)
    if sorted(lst_A) == sorted(lst_B):
        print(f"{A} & {B} are anagrams.")
    else:
        print(f"{A} & {B} are NOT anagrams.")