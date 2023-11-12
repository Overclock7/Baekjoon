# https://www.acmicpc.net/problem/5637

import sys
import re

input = sys.stdin.readline

words = list()
while True:
    words.extend(input().rstrip().split()) # 한 줄의 모든 단어를 리스트에 추가
    if words[-1] == 'E-N-D':
        break

result = list()
for i in words:
    result.append(re.sub('[^a-z-]',"",i.lower())) # a-z , - 를 제외한 문자 제거

print(sorted(result,key= lambda x: -len(x))[0])

# 2 (Baekjoon)

# import sys
# import re
# article = sys.stdin.readlines()
# cond = re.compile(r'[a-zA-z-]+')
# longest = ''
# for sent in article:
#     words = cond.findall(sent)
#     for word in words:
#         if len(word)>len(longest):
#             longest = word
# print(longest.lower())

# 3 (Baekjoon)

# import re
# import sys

# def find_longest_word(text):
    
#     words = re.findall(r'\b[a-zA-Z-]+\b', text) # Using regex to find all words which contain letters and possibly hyphens

#     longest_word = max(words, key=len, default='') # Finding the longest word
    
#     return longest_word.lower()


# text = [] # Reading input
# for line in sys.stdin:
#     line = line.strip()
#     if line == 'E-N-D':
#         break
#     text.append(line)

# text = ' '.join(text)
# print(find_longest_word(text))