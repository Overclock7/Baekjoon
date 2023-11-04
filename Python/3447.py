# https://www.acmicpc.net/problem/3447

with open(0) as f:
    for s in f:
        while 'BUG' in s:
            s = s.replace('BUG','')
        print(s,end="")

#2 (Overclock0708)

# while True:
#     try:
#         s = input()
#         while "BUG" in s:
#             s = s.replace("BUG","")
#         print(s)
#     except:
#         break
