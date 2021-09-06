"""
https://www.acmicpc.net/problem/20943

카카오톡

난이도: 골드 4

시작: 21.08.27 11:36
끝: 21.05.11 12:13
성공: 

메모리:  KB
시간:   ms

[아이디어]
기울기가 다르면 직선은 만난다.

순서쌍을 b로 나눈다.
키: 기울기(a/b), value: y절편(c/b)가 되게 딕셔너리에 넣는다.

b가 0이면,,

d = {3: {1: 2, 2.33}, 2:{1: 1.5, 2.5}}


[시간복잡도]



[실수]



[검색]



[개선/추가사항]



[고수풀이]
링크: 

메모리:  KB
시간:   ms


접근법:


배울 점: 


코드



"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
arr = list(map(int, input().split()))

print(" ".join(map(str,arr)) + "\n")