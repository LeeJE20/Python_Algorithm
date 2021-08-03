"""
https://www.acmicpc.net/problem/11053

가장 긴 증가하는 부분 수열

시작: 21.05.24 20:39
끝: 21.05.11 12:13
성공: 

메모리:  KB
시간:   ms

[아이디어]
1. set
2. sort
3. print(len(sort))


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

N = int(input())
arr = list(map(int, input().split()))

print(set(arr))
