"""
https://www.acmicpc.net/problem/11399

ATM

시작: 21.05.23 17:18
끝: 21.05.23 17:28
성공: correct
메모리: 29200 KB
시간: 76 ms


[아이디어]
그리디로 풀면 되겠다.



정렬하고 다음 수행
for i in range(n)
    sum += arr[i] * (n-i)
설명: 0번째 사람의 작업은 나머지 n-1명이 모두 기다려야 하며, 0번째 사람에게도 걸리는 시간이다.
2번째 사람의 작업은 나머지 n-2명이 모두 기다려야 한다.


[시간복잡도]
정렬-> nlogn


[실수]
N을 n으로 썼다.

[검색]
(처음에 사람 번호를 출력해야 하는줄 알고 딕셔너리 써야겠다고 생각했었다)
딕셔너리 정렬
https://velog.io/@kylexid/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%97%90%EC%84%9C-%EB%94%95%EC%85%94%EB%84%88%EB%A6%AC-%EC%9E%90%EB%A3%8C-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0

[개선/추가사항]



고수풀이]
https://www.acmicpc.net/user/2015136076

메모리: 29284 KB
시간: 52 ms

나랑 거의 같은데, 시간 계산을 곱으로 안 하고 그 사람까지의 수행시간을 더했다.
sort 리턴도 딱히 안 했다.

배울 점: 모르겠다. 뭘 배워야 하지? 내 풀이는 왜 느린지 모르겠다.
sorted는 새로운 변수에 할당하는게 힘들었나?

a = int(input())
l = []
total = 0
cur = 0
l = list(map(int, input().split()))

l.sort()
for x in l:
    cur += x
    total += cur
print(total)


고수풀이2]
https://www.acmicpc.net/source/18388663

메모리: 29284 KB
시간: 52 ms

위와 같은 접근
배울 점: sorted를 따로 저장하지 않고 for i in sorted(a)의 식으로 하였다.
import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))

time = 0
sum = 0
for i in sorted(a):
    time = i + time
    sum += time

print(sum)


"""

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)

sum = 0
for i in range(N):
    sum += arr[i] * (N-i)

print(sum)

