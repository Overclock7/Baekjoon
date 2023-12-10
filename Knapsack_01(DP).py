
# n = # of items
# w = max_weight
# items = (weight, benefit) , items[0] = [0,0] 
def Knapsack(N,W,items):
    
    # 총 무게 w에서 item k번째까지 고려했을 때의 가장 최대 이익
    benefit = [[0 for _ in range(W+1)] for _ in range(N+1)]
    
    for ik in range(1,N+1): # 현재 아이템 개수 ik
        for wk in range(1,W+1): # 현재 총 무게 wk
            if items[ik][0] <= wk: # ik번째 아이템의 무게 < 현재 총 무게 wk
                benefit[ik][wk] = max(benefit[ik-1][wk],benefit[ik-1][wk-items[ik][0]] + items[ik][1])
            else:
                benefit[ik][wk] = benefit[ik-1][wk]
    
    return(benefit[N][W])

N = 4
M = 10
items = [   [0,0], # items[0]은 Index를 맞추기 위해 안 씀
            [3,5],[4,2],[3,3],[2,7]
        ]

print(Knapsack(N,M,items))