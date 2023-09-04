T = int(input())
for i in range(T):
    N = int(input())
    Dic = dict()
    for j in range(N):
        Univ, Alc = input().split()
        Dic[int(Alc)] = Univ
    print(Dic[max(Dic.keys())])