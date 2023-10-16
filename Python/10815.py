# https://www.acmicpc.net/problem/10815

import sys
input = sys.stdin.readline

n = int(input())
card = dict()

for c in map(int,input().rstrip().split()):
    if c not in card.keys():
        card[c] = 1

m = int(input())
for question in map(int,input().rstrip().split()):
    if question in card:
        print(1 , end = " ")
    else :
        print(0 , end = " ")
