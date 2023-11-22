# 3학년 2학기 알고리즘 수업 내용

def BruteForce(text,pattern):
    
    t_len = len(text)
    p_len = len(pattern)
    
    for i in range(t_len):
        j = 0
        while j < p_len and text[i+j] == pattern[j]:
            j += 1
        if j == p_len :
            return i
    return -1
"""------------------------------------------------------------"""
def Hash(text,hash_len):
    hash = 0
    for i in range(hash_len):
        hash = 2 * hash + ord(text[i])
    return hash

def Rehash(start,hash,text,len_hash):
    rehash = 2 * (hash - (ord(text[start]) << (len_hash - 1))) + ord(text[start+len_hash])
    return rehash

def KarpRobin(text,pattern):
    t_len = len(text)
    p_len = len(pattern)
    hash_text = Hash(text,p_len)
    hash_pattern = Hash(pattern,p_len)
    
    for i in range((t_len - p_len) + 1):
        if hash_text == hash_pattern:
            j = 0
            while j < p_len and text[i+j] == pattern[j]:
                j += 1
            if j == p_len :
                return i
        hash_text = Rehash(i,hash_text,text,p_len)
    return -1
"""------------------------------------------------------------"""
def Border_KMP(pattern): # 강의 PPT와 다름
    p_len = len(pattern)
    border = list(0 for _ in range(p_len + 1))
    border[0] = -1
    
    index = 1
    pointer = 0 # 반복되는 패턴의 끝을 가리킴
    
    while index < p_len :
        if pattern[index - 1] == pattern[pointer]:
            pointer += 1
            border[index] = pointer
            index += 1
        elif pointer > 0: # 안맞으면, pointer를 다음 반복되는 곳으로 이동
            pointer = border[pointer] # 직접 그려보면서 해볼 것
        else: # 안맞으면 border[i] = 0
            border[index] = 0
            index += 1
    
    return border

def KMP(text,pattern,border):
    t_len = len(text)
    p_len = len(pattern)
    t_idx = 0
    p_idx = 0
    
    while t_idx + p_idx < t_len:
        if pattern[p_idx] == text[t_idx + p_idx]:
            if p_idx == p_len - 1:
                return t_idx
            p_idx += 1
        else:
            if border[p_idx] > -1:
                t_idx = t_idx + p_idx - border[p_idx] # 규칙
                p_idx = border[p_idx]
            else: # border[p_idx] == -1 인 경우
                t_idx = t_idx + 1 # 한 칸 이동
                p_idx = 0 # 패턴 첫번째로
"""------------------------------------------------------------"""

text =  "abcdefgcaac"
pattern = 'c'

print("BruteForce : %d"%BruteForce(text,pattern))
print("KarpRobin : %d"%KarpRobin(text,pattern))
print("KMP : %d"%KMP(text,pattern,Border_KMP(pattern)))