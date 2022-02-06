'''idea
https://www.acmicpc.net/problem/1764

해시테이블 이용- 딕셔너리 사용
시작: 22-02-06 11:37
correct: 2022-02-07 12:09

보완: 
1) 그냥 집합 연산 쓰면 된다..
2) 이름들을 전부다 받고 문자열 슬라이싱으로 분리해도 된다.
'''
import sys
from collections import defaultdict

read = sys.stdin.readline
print= sys.stdout.write

N, M = list(map(int, read().split()))
not_heard = defaultdict(bool)
for i in range (N):
    item = read().strip()
    not_heard[item] = True

result = []
for _ in range (M):
    not_seen = read().strip()
    if not_seen in not_heard:
        result.append(not_seen)

print(str(len(result))+'\n')
print('\n'.join(sorted(result)))
