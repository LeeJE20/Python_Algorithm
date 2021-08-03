"""
https://www.acmicpc.net/problem/11726


시작: 21.05.23 17:48
끝: 21.05.23 18:08
성공: correct

메모리: 29200 KB
시간:  80 ms

[아이디어]
n을 1과 2의 합으로 나타낼 수 있는 경우의 수 문제

오늘도 DP이다.

d[n] = d[n-1] + d[n-2]

합이 10007보다 크면, 10007로 나눈 나머지를 d에 채운다.


[시간복잡도]



[실수]


[검색]


[개선/추가사항]


고수풀이]

"""


import sys
input = sys.stdin.readline
n = int(input())
# arr = list(map(int, input().split()))

# 인덱스 에러 났길래 n+1에서 n+2로 고쳐봄..
d = [0 for _ in range(n+2)]

d[1] = 1
d[2] = 2

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
    # 실수: 10007로 나눈 나머지 부분을 까먹고 코드로 작성하지 않았다.
    if d[i] >= 10007:
        d[i]%=10007

print(d[n])