V = int(input())
Result = list(input())
if Result.count('A') > Result.count('B'):
    print('A')
elif Result.count('A') < Result.count('B'):
    print('B')
else :
    print('Tie')