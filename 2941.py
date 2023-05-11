s = input()
minus = 0

#dz=는 2번 세어야 하나 , z = 때문에 자연스레 한번 세어진다.
minus += s.count('c=')
minus += s.count('c-')
minus += s.count('dz=') 
minus += s.count('d-')
minus += s.count('lj')
minus += s.count('nj')
minus += s.count('s=')
minus += s.count('z=')

count = len(s) - minus

print(count)
