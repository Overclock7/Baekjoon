while True:
    tri = list(map(int,input().split()))

    if tri == [0,0,0] :
        break

    tri.sort()

    if tri[2] >= tri[1] + tri[0]:
        print('Invalid')
    elif tri[2] == tri[1] == tri[0]:
        print('Equilateral')
    elif tri[2] == tri[1] or tri[1] == tri[0] or tri[0] == tri[2]:
        print('Isosceles')
    else:
        print('Scalene')
