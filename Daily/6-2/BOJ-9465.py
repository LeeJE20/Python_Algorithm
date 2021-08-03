"""
https://www.acmicpc.net/problem/9465

스티커

난이도: 실버 2

시작: 21.06.06 21:36
끝: 21.06.06 22:11
성공: 

메모리: 40164 KB
시간:  	1128 ms

2차시도:
메모리: 37828 KB
시간:  	800 ms

[아이디어]
돌 놓기 문제다!
dp로 풀면 된다.

스티커를 안 떼는 경우, 위쪽을 떼는 경우, 아래쪽을 떼는 경우로 나눈다.

sticker[2][n]


dp[3][n] = [[0 for _ in range(n)] * 3 ]

dp[0][n] : n번째에 위쪽 스티커를 떼는 경우
dp[1][n]: n번째에 아래쪽 스티커를 떼는 경우
dp[2][n]: n번째에 스티커를 안 떼는 경우

# 초기화
dp[0][0] = sticker[0][0]
dp[1][0] = sticker[1][0]
dp[2][0] = 0

타뷸레이션으로 풀자.
for i in range()

# 이전열에서 스티커를 어떻게 했든 이번 열에서는 안 뗄 수 있다
dp[2][n] = max(dp[0][n-1], dp[1][n-1], dp[2][n-1])

# 이전열에서 스티커를 안 떼거나 아래쪽 스티커를 뗀 경우에만, 이번 열에서 위쪽 스티커를 뗄 수 있다.
dp[0][n] = max(dp[1][n-1], dp[2][n-1]) + 위쪽 스티커 점수

# 이전열에서 스티커를 안 떼거나 위쪽 스티커를 뗀 경우에만, 이번 열에서 아래쪽 스티커를 뗄 수 있다.
dp[1][n] = max(dp[0][n-1], dp[2][n-1]) + 아래쪽 스티커 점수

[시간복잡도]
테이블 한 번만 훑으면 되므로 O(n)


[실수]
    # 실수: [[0 for _ in range(n)]* 3 ] 으로 했더니 1차원 리스트가 생성되었다.
    dp = [[0] * n for _ in range (3) ]


    # 실수: sys.stdout.write는 str을 인자로 주고, 끝에 +\n을 붙여야 한다
    print(str(max(dp[0][n-1], dp[1][n-1], dp[2][n-1]))+"\n")

[검색]



[개선/추가사항]
아이디어 구현은 보자마자 했는데, 배열 순서가 꼬여서 그거 고치는게 오래 걸렸다.
처음에는 첫 번째 인덱스를 열(n)로 하고, 두 번째 인덱스를 행(2)으로 하려고 했다.
그런데 문제 입력 받는 곳을 보니 데이터를 한 행을 통째로 입력받게 되어 있어서 뒤늦게 인덱스 순서를 다 고쳐야 했다.
다음에 2차원 배열이 나오면 입출력 데이터 모양을 먼저 보고 모양을 결정해야겠다.



[고수풀이]
링크: https://www.acmicpc.net/source/26635488

메모리: 37560 KB
시간:  712 ms


접근법: 완벽하게 똑같다.


배울 점: 


코드



"""

import sys
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())

# def solve():
#     n = int(input())
#     sticker = [list(map(int, input().rstrip().split())) for _ in range(2)]
#     # print(sticker)

#     # 실수: [[0 for _ in range(n)]* 3 ] 으로 했더니 1차원 리스트가 생성되었다.
#     dp = [[0] * n for _ in range (3) ]
#     # print(dp)
#     # dp[0][n] : n번째에 위쪽 스티커를 떼는 경우
#     # dp[1][n]: n번째에 아래쪽 스티커를 떼는 경우
#     # dp[2][n]: n번째에 스티커를 안 떼는 경우

#     # 초기화
#     dp[0][0] = sticker[0][0]
#     dp[1][0] = sticker[1][0]
#     dp[2][0] = 0

#     #타뷸레이션으로 풀자.
#     for i in range(1, n):

#         # 이전열에서 스티커를 어떻게 했든 이번 열에서는 안 뗄 수 있다
#         dp[2][i] = max(dp[0][i-1], dp[1][i-1], dp[2][i-1])

#         # 이전열에서 스티커를 안 떼거나 아래쪽 스티커를 뗀 경우에만, 이번 열에서 위쪽 스티커를 뗄 수 있다.
#         dp[0][i] = max(dp[1][i-1], dp[2][i-1]) + sticker[0][i]

#         # 이전열에서 스티커를 안 떼거나 위쪽 스티커를 뗀 경우에만, 이번 열에서 아래쪽 스티커를 뗄 수 있다.
#         dp[1][i] = max(dp[0][i-1], dp[2][i-1]) + sticker[1][i]

#     # 실수: sys.stdout.write는 str을 인자로 주고, 끝에 +\n을 붙여야 한다
#     print(str(max(dp[0][n-1], dp[1][n-1], dp[2][n-1]))+"\n")


# dp 테이블 안 쓰고 변수만으로 처리
def solve2():
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    up = sticker[0][0]
    down = sticker[1][0]
    no = 0

    for i in range(1, n):
        up, down, no = max(down, no) + sticker[0][i], max(up, no) + sticker[1][i], max(up, down, no)

    print(str(max(up, down, no))+"\n")
for _ in range(N):
    solve2()