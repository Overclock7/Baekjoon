# https://www.acmicpc.net/problem/1966

T = int(input())

for _ in range(T):
    N, M = map(int,input().split())
    print_queue = [[sequence,int(priority)] for sequence, priority in enumerate(input().split())]
    print_num = 0

    while True:
        if print_queue[0][1] == max(print_queue,key = lambda x: x[1])[1]: # priority 

            print_num += 1

            if print_queue[0][0] == M : #sequence
                print(print_num)
                break
            else:
                print_queue.pop(0) # dequeue
        else:
            print_queue.append(print_queue.pop(0)) # dequeue and enqueue

# Beakjoon