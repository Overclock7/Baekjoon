# https://www.acmicpc.net/problem/13220

import sys
input = sys.stdin.readline

def make_kmp_table(pattern, border):
    m = len(pattern)
    border[0] = -1

    i = 1
    cnd = 0

    while i < m :
        if pattern[i-1] == pattern[cnd]: # 문자열이 같은 경우
            cnd += 1
            border[i] = cnd 
            i += 1
        elif cnd > 0:
            cnd = border[cnd] # 문자열이 다른데 cnd가 0이 아닐 경우 -> 다음 패턴의 끝으로 옮김
        else:
            border[i] = 0
            i += 1

def kmp_search(pattern, border, text):
    m = 0
    i = 0
    t_len = len(text)
    p_len = len(pattern)

    while m+i < t_len:
        if pattern[i] == text[m+i]: # Pattern과 Text 비교
            if i == p_len-1:
                return m
            i += 1
        else:                       # Pattern index = i , Text index = m + i 에서 틀림
            if border[i] > -1:
                m = m + i - border[i] # Text index 는 (Error 난 곳) - (Border[i])
                i = border[i] # Pattern index는 Border[i]
            else: # border[i] == 0 이면 한 칸 이동
                i = 0
                m += 1

    return -1

if __name__ == '__main__' :
    N = int(input())
    text = list(map(int,input().rstrip().split())) * 2
    pattern = list(map(int,input().rstrip().split()))
    border = list(0 for _ in range(N))

    make_kmp_table(pattern,border)
    result = kmp_search(pattern,border,text)

    if result == -1:
        print('NO')
    else:
        print('YES')

