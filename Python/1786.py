# https://www.acmicpc.net/problem/1786

def Border_KMP(pattern):
    len_pattern = len(pattern)
    border = list(0 for _ in range(len_pattern + 1))
    border[0] = -1 # type: ignore
    border[1] = 0
    
    index = 2
    pointer = 0 # 반복되는 패턴의 끝을 가리킴
    
    while index < len_pattern :
        if pattern[index - 1] == pattern[pointer]:
            pointer += 1
            border[index] = pointer # type: ignore
            index += 1
        elif pointer > 0: # 안맞으면, pointer를 다음 반복되는 곳으로 이동 (직접 그려보면서 할 것!)
            pointer = border[pointer]
        else: # 안맞으면 border[i] = 0
            border[index] = 0
            index += 1
    
    return border

def KMP(text,pattern,border):
    len_text = len(text)
    len_pattern = len(pattern)
    index_text = 0 # 기준 index = 0 / 문제에서는 index = 1로 시작
    index_pattern = 0
    result = list() #기존 코드 추가
    
    while index_text + index_pattern < len_text:
        if pattern[index_pattern] == text[index_text + index_pattern]:
            if index_pattern == len_pattern - 1:
                result.append(index_text + 1) # 기존 코드 변경
                index_text = index_text + index_pattern - border[index_pattern]
                index_pattern = border[index_pattern]
                continue
            index_pattern += 1         
        else:
            if border[index_pattern] > -1:
                index_text = index_text + index_pattern - border[index_pattern]
                index_pattern = border[index_pattern]
            else:
                index_text = index_text + 1
                index_pattern = 0
    
    print(len(result))
    print(*result)

with open(0) as f:
    text = f.readline().rstrip()
    pattern = f.readline().rstrip()
KMP(text,pattern,Border_KMP(pattern))

# 2 (Baekjoon)

# def Border_KMP(pattern):
#     len_pattern = len(pattern)
#     border = list(0 for _ in range(len_pattern))
    
#     j = 0
#     for i in range(1,len_pattern):
#         while j > 0 and pattern[i] != pattern[j]:
#             j = border[j-1]
#         if pattern[i] == pattern[j]:
#             j += 1
#             border[i] = j
            
#     return border

# def KMP(text,pattern):
#     len_text = len(text)
#     len_pattern = len(pattern)
#     border = Border_KMP(pattern)
#     result = list() #기존 코드 추가
    
#     j = 0
#     for i in range(len_text):
#         while j > 0 and text[i] != pattern[j]:
#             j = border[j-1]
#         if text[i] == pattern [j]:
#             if j == len_pattern - 1:
#                 result.append(i - len_pattern + 2)
#                 j = border[j]
#             else:
#                 j += 1
    
#     print(len(result))
#     print(*result)

# with open(0) as f:
#     text = f.readline().rstrip()
#     pattern = f.readline().rstrip()
# KMP(text,pattern)

