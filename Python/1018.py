# https://www.acmicpc.net/problem/1018

M, N = map(int,input().split())
B_list = ["BWBWBWBW", #Black First
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB"]
W_list = ["WBWBWBWB", #White First
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW"]

board = []
min_diff = 64
for i in range(M):
    board.append(input().strip())

for row in range(M-7):
    for col in range(N-7):
        B_diff, W_diff = 0, 0
        for i in range(8):
            for j in range(8):
                if board[row+i][col+j] != B_list[i][j]:
                    B_diff += 1
                if board[row+i][col+j] != W_list[i][j]:
                    W_diff += 1
        min_diff = min(min_diff,B_diff,W_diff)

print(min_diff)