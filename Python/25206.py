# https://www.acmicpc.net/problem/25206

grade_dict = {"A+":4.5,'A0':4.0,'B+':3.5,"B0":3.0,"C+":2.5,"C0":2.0,"D+":1.5,"D0":1.0,"F":0.0}

score_total = 0
result = 0

for i in range(20):
    name, score, grade = input().split()
    score = float(score)
    if grade != 'P':
        score_total += score
        result += score*grade_dict[grade]

print('%.6f'%(result/score_total))

