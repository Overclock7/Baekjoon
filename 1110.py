import sys

s = int(sys.stdin.readline())

s1 = int(s/10)
s0 = int(s % 10)
cycle = 0

while (True):
    cycle += 1
    new_s0 = int((s1+s0) % 10)
    s1 = s0
    s0 = new_s0
    check = s1*10 + s0
    if (check == s):
        print(cycle)
        break
