
n = int(input())

for i in range(n):
    count = 0
    inputs = list(map(int,input().split()))
    scores = inputs[1:]
    average = sum(scores)/len(scores)

    for i in scores:
        if i > average:
            count +=1

    print(f'{count/len(scores)*100:.3f}%')