# 3학년 2학기 알고리즘 수업 내용

def BruteForce(text,pattern):
    
    len_text = len(text)
    len_pattern = len(pattern)
    
    for i in range(len_text):
        j = 0
        while j < len_pattern and text[i+j] == pattern[j]:
            j += 1
        if j == len_pattern :
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
    len_text = len(text)
    len_pattern = len(pattern)
    hash_text = Hash(text,len_pattern)
    hash_pattern = Hash(pattern,len_pattern)
    
    for i in range((len_text - len_pattern) + 1):
        if hash_text == hash_pattern:
            j = 0
            while j < len_pattern and text[i+j] == pattern[j]:
                j += 1
            if j == len_pattern :
                return i
        hash_text = Rehash(i,hash_text,text,len_pattern)
    return -1
"""------------------------------------------------------------"""
def Border_KMP(pattern): # 강의 PPT와 다름
    len_pattern = len(pattern)
    border = list(0 for _ in range(len_pattern + 1))
    border[0] = -1
    
    index = 1
    pointer = 0 # 반복되는 패턴의 끝을 가리킴
    
    while index < len_pattern :
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
    len_text = len(text)
    len_pattern = len(pattern)
    index_text = 0
    index_pattern = 0
    
    while index_text + index_pattern < len_text:
        if pattern[index_pattern] == text[index_text + index_pattern]:
            if index_pattern == len_pattern - 1:
                return index_text
            index_pattern += 1
        else:
            if border[index_pattern] > -1:
                index_text = index_text + index_pattern - border[index_pattern] # 규칙
                index_pattern = border[index_pattern]
            else: # border[index_pattern] == -1 인 경우
                index_text = index_text + 1 # 한 칸 이동
                index_pattern = 0 # 패턴 첫번째로
"""------------------------------------------------------------"""

text =  "abcdefgcaac"
pattern = 'c'

print("BruteForce : %d"%BruteForce(text,pattern))
print("KarpRobin : %d"%KarpRobin(text,pattern))
print("KMP : %d"%KMP(text,pattern,Border_KMP(pattern)))