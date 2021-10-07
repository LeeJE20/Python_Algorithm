"""
https://www.acmicpc.net/problem/1012

유기농 배추

난이도: 실버 2 (체감: 중상. 공부하기 좋은 난이도)

시작: 21.05.26 19:47
끝: 21.05.26 21:22
성공: correct

메모리: 29200 KB
시간:  84 ms

[아이디어]
오른쪽, 아래쪽
재귀

한번 체크한 곳은 -1로 체크


[시간복잡도]
음,,, n개를 전부 훑어야 하므로 O(n)


[실수]

꺾인 ㄴ 모양이면 왼쪽으로 가는 것도 체크해줘야 한다!!
[0, 1, 0]
[1, 1, 0]
[0, 0, 0]

 (x, y) = (1, 0) 도착
[0, 2, 0]
[1, 1, 0]
[0, 0, 0]

 (x, y) = (1, 1) 도착
[0, 2, 0]
[1, 2, 0]
[0, 0, 0]
count증가 : 1

 (x, y) = (0, 1) 도착
[0, 2, 0]
[2, 2, 0]
[0, 0, 0]
count증가 : 2

U 모양도 반례이다.
즉, 오른쪽, 아래, 왼쪽, 위 모두 체크 해야 한다



# 실수: result가 int이면 조인이 안 된다.
# solve()가 str을 리턴하게 했다.

[검색]
- 함수 파라미터: mutable 객체는 call by reference처럼 된다
- 재귀함수를 스택으로 만들기
https://comdoc.tistory.com/entry/10-스택과-재귀recursive-파이썬


[개선/추가사항]
처음에는 arr를 오른쪽, 아래쪽으로 하나씩 훑어 나가므로 재귀로 같은 영역인지 확인할 때도 오른쪽, 아래만 확인하면 된다고 생각했다.
히지만 ㄹ 모양이나 U 모양 등의 반례가 존재한다.

추후 비슷한 문제를 만나면 ㄹ 모양처럼 복잡한 모양의 예도 적용되는지 생각해봐야겠다.
(아님 일단 문제를 푸는 것이 중요하니 상하좌우 다 돌게 만들거나..)

내 풀이 중 find를 쓰는 풀이는 왜 RecursionError가 생기는지 모르겠다.


[고수풀이]
링크: https://www.acmicpc.net/source/14558062

메모리: 30048 KB
시간:  64 ms


접근법:
나랑 같다.

배울 점: 
    if o+1 < x and t[s][o+1]==1:
        T(t,o+1,s)
이런 식으로 재귀함수에 들어간 다음 아니면 리턴하지 말고, 
되는 경우에만 재귀 함수에 들어가도록 해봐야겠다.

아 근데 나랑 접근법은 같은데 왜 내가 재귀함수 썼을 때는 RecursionError가 난 걸까..

코드

import sys;p=sys.stdin.readline;
sys.setrecursionlimit(1000000)
q=int(p())
def T(t, o, s):
    t[s][o]=0
    if o+1 < x and t[s][o+1]==1:
        T(t,o+1,s)
    if o-1>= 0 and t[s][o-1]==1:
        T(t, o-1,s)
    if s -1 >= 0 and t[s-1][o]==1:
        T(t, o,s-1)
    if s +1 < y and t[s+1][o]==1:
        T(t,o,s+1)

for _ in range(q):
    x, y, c = map(int, p().split())
    t = [[0] * x for _ in range(y)]
    for i in range(0,c):
        m,n=map(int,p().split());t[n][m] = 1
    v = 0
    for i in range(0,x):
        for j in range(0, y):
            if t[j][i] == 1:
                T(t, i, j);v+=1
    print(v)




"""

import sys
input = sys.stdin.readline


def solve() -> str:
    # ~~ 입력 받기

    # 가로 M, 세로 N, 배추의 위치 개수 K
    M, N, K = map(int, input().split())
    # 오른쪽, 왼쪽, 아래쪽, 위쪽에 껍질을 씌워준다. (범위 벗어남 계산 안 해도 됨)
    arr = [[0] * (M+2) for _ in range(N+2)]
    # 배추의 위치 표시
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y+1][X+1] = 1

    # 결과
    count = 0

    # print("\n".join(map(str, arr)))

    # ~~ 검사

    # 밭을 하나씩 루프 돈다.
    for y in range (1, N+1):
        for x in range(1, M+1):
            # 배추가 있으면, 연결된 곳을 모두 찾는다.
            if arr[y][x] == 1:
                find4(arr, y, x)
                count += 1
                # print(f"count증가 : {count}")

    return str(count)
    
# 재귀
# 연결된 배추 찾기
# mutable 객체는 call by reference처럼 된다.
# x, y는 현재 위치
def find(arr: list, y: int, x: int):
    if arr[y][x] == 2 or arr[y][x] == 0:
        return
    else: # 1인 경우
        # 도착한 적 있다고 체크
        arr[y][x] = 2

        # print(f"\n (x, y) = ({x}, {y}) 도착")
        # print("\n".join(map(str, arr)))

        # 오른쪽, 아래쪽, 왼쪽, 위쪽 탐색
        find(arr, y, x+1)
        find(arr, y+1, x)
        find(arr, y, x-1)
        find(arr, y-1, x)


# 고수 처럼 if문 써서 재귀를 돌지 말지 체크
def find4(arr: list, y: int, x: int):
    # 도착한 적 있다고 체크
    arr[y][x] = 2

    # print(f"\n (x, y) = ({x}, {y}) 도착")
    # print("\n".join(map(str, arr)))

    # 오른쪽, 아래쪽, 왼쪽, 위쪽 탐색
    if (arr[y][x+1] == 1):
        find(arr, y, x+1)
    if (arr[y+1][x] == 1):
        find(arr, y+1, x)
    if (arr[y][x-1] == 1):
        find(arr, y, x-1)
    if (arr[y-1][x] == 1):
        find(arr, y-1, x)



# 스택 사용 https://www.acmicpc.net/board/view/67183
# https://comdoc.tistory.com/entry/10-스택과-재귀recursive-파이썬
# 연결된 배추 찾기
# mutable 객체는 call by reference처럼 된다.
# x, y는 현재 위치
def find2(arr: list, y: int, x: int):
    stack = []
    # 우, 하, 좌, 상
    next = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    arr[y][x] = 2
    stack.append([y, x])

    while stack:
        n, m = stack.pop()
        # 도착한 적 있다고 체크
        

        # 우, 하, 좌, 상 중 갈 곳을 스택에 넣는다.
        for j, i in next:
            yy = n+j
            xx = m+i
            # 갈 수 있다면
            if arr[yy][xx] == 1: 
                arr[yy][xx] = 2
                stack.append([yy, xx])





# find3 함수 사용
def solve2() -> str:
    # ~~ 입력 받기

    # 가로 M, 세로 N, 배추의 위치 개수 K
    M, N, K = map(int, input().split())
    # 오른쪽, 왼쪽, 아래쪽, 위쪽에 껍질을 씌워준다. (범위 벗어남 계산 안 해도 됨)
    arr = [[0] * (M+2) for _ in range(N+2)]
    # 배추의 위치 표시
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y+1][X+1] = 1

    # 결과
    count = 0

    print("\n".join(map(str, arr)))

    # ~~ 검사

    # 밭을 하나씩 루프 돈다.
    for y in range (1, N+1):
        for x in range(1, M+1):
            # 배추가 있으면, 연결된 곳을 모두 찾는다.
            if arr[y][x] == 1:
                count += find3(arr, y, x)
                print(f"count: {count}")


    return str(count)


# 틀림. 반례 존재
# [0, 0, 0, 0, 0, 0, 0]
# [0, 2, 0, 2, 3, 2, 0]
# [0, 2, 0, 2, 0, 2, 0]
# [0, 2, 2, 2, 0, 2, 0]
# [0, 0, 0, 0, 0, 0, 0]
def find3(arr: list, y: int, x: int) -> int:
    stack = []
    # 우, 하
    next = [[0, 1], [1, 0]]
    arr[y][x] = 2
    stack.append([y, x])

    while stack:
        n, m = stack.pop()
        # 도착한 적 있다고 체크
        arr[n][m] = 2

        print(f"\n (x, y) = ({x}, {y}) 도착")
        print("\n".join(map(str, arr)))
        # 우, 하, 좌, 상 중 갈 곳을 스택에 넣는다.
        for j, i in next:
            yy = n+j
            xx = m+i
            # 갈 수 있다면
            if arr[yy][xx] == 1: 
                arr[yy][xx] = 3 # 갈 곳이라는 체크
                stack.append([yy, xx])
            # 연결된 것 중에 이미 간 곳이 있다면
            # 이미 찾은 덩어리이다.
            if arr[yy][xx] == 2:
                print(f"\n (x, y) = ({x}, {y}) 이미 연결된 덩어리")
                return 0
        print(f"\n (x, y) = ({x}, {y}) 갈 곳 체크")
        print("\n".join(map(str, arr)))
    return 1

        
    


T = int(input())
result = [0] * T

for i in range(T):
    result[i] = solve()


# 재귀 리미트 걸렸다...
sys.setrecursionlimit(10**7)


# 실수: result가 int이면 조인이 안 된다.
# solve()가 str을 리턴하게 했다.

# 다른 방법 print(" ".join(map(str, num_list)))
print('\n'.join(result))