"""
https://www.acmicpc.net/problem/18870

좌표 압축

난이도: 실버 2

시작: 21.05.27 20:06
끝: 21.05.27 20:19
성공: correct

메모리: 272680 KB
시간:  3192 ms

[아이디어]
정렬
해시?
 


디폴트 딕셔너리 : 리스트
key: 좌표
value: [그 좌표가 나온 순서]

리스트 result:  결과값을 저장할 리스트

리스트 locations: 입력받은 좌표들



1. location = list(set(location)).sort
집합으로 중복 제거 -> 리스트로 다시 만들기 -> 정렬

2. 


for i, v in enumerate(location):
    딕셔너리[v]의 순서들에 대하여:
        result[순서] = i
예)
1 2 3 4 8

1보다 작은 것은 0개이다. (인덱스가 0이므로)

8보다 작은 것은 4개이다( 인덱스가 8이므로)

[시간복잡도]
set: n
소트-> nlogn

[실수]
print(' '.join(result))
result에는 str만 있어야 한다.

.sort()는 값을 반환하지 않는다.


[검색]
enumerate 리턴값: 튜플이다.
(인덱스, 값)


[개선/추가사항]



[고수풀이]
링크: https://www.acmicpc.net/source/21803521

메모리: 198884 KB
시간:  1576 ms


접근법:


배울 점: 
매우 파이써닉하다.

1. set은 sorted하면 list를 리턴한다.
2. for문 돌릴 용도의 리스트는 in ~~~에서 계산식을 넣어도 된다.
따로 변수로 갖고 있을 필요가 없다.
3. 파이썬의 map은 리스트의 각 요소에 대해 함수를 실행시켜준다.
4. 결과를 result 변수에 안 담고도 마지막에 바로 출력 가능하다.

코드
import sys
input = sys.stdin.readline
input()
tmp = list(map(int, input().split()))
x = dict()
for idx, num in enumerate(sorted(set(tmp))):
    x[num] = idx
sys.stdout.write(' '.join(map(str,(x[num] for num in tmp))))


"""


#sys.stdout.write(' '.join(result))
import sys
input = sys.stdin.readline

from collections import defaultdict

# key: 좌표
# value: [그 좌표가 나온 순서]
d = defaultdict(list)
N = int(input())

# 리스트 locations: 입력받은 좌표들
locations = list(map(int, input().split()))

# 리스트 result:  결과값을 저장할 리스트
result = [0] * N

# print(locations)

for i, v in enumerate(locations):
    # insert 말고 append 써야 한다
    # d[v].insert(i)
    d[v].append(i)
    # print("index : {}, value: {}".format(i,v))

# 집합으로 중복 제거 -> 리스트로 다시 만들기 -> 정렬
# locations = list(set(locations)).sort
# error: TypeError: 'NoneType' object is not iterable
locations = sorted(list(set(locations)))

for i, v in enumerate(locations):
    # 딕셔너리[v]의 순서들에 대하여:
    for order in d[v]:
        # result[순서] = i
        result[order] = str(i)


print(' '.join(result))
# sys.stdout.write(' '.join(result))