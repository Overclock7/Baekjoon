while True:
    n = int(input())
    if n == -1:
        break
    li = []

    for i in range(1,n):
        if n % i == 0:
            li.append(i)

    if sum(li) == n:
        print(f"{n} =",end="")
        for i in li:
            if i != li[len(li)-1]:
                print(f' {i} +',end="")
            else:
                print(f' {i}')
    else:
        print(f"{n} is NOT perfect.")    
