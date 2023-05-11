
n = int(input())
l = list()

if n < 100:
    print(n)
else:
    for i in range(100,n+1):
        j = list(str(i))
        if i < 1000:
            if((int(j[0]) - int(j[1])) == (int(j[1]) - int(j[2]))):
                l.append(i)
        else :
            if((int(j[0])-int(j[1])) == (int(j[1])-int(j[2])) and (int(j[1])-int(j[2])) == (int(j[2])-int(j[3]))):
                l.append(i)
    print(99+len(l))