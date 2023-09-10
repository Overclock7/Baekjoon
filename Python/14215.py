# https://www.acmicpc.net/problem/14215

tri = list(map(int,input().split()))
tri.sort()

if tri[2] >= tri[1] + tri[0]:
    print(2 * (tri[1] + tri[0]) - 1)
else:
    print(tri[2] + tri[1] + tri[0])
