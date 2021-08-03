"""
https://www.acmicpc.net/problem/1463
1로 만들기


시작: 21.05.21 12:40
끝: 21.05.21 13:54
성공: correct

[아이디어]

아이디어1)
프로그래머스에서 비슷한 문제를 풀었다.

반대로 생각하기..

1로 시작하여 N을 만든다
bfs, 재귀

연산 1, 2, 3 을 반대로 실행
연산1) 곱하기3
연산2) 곱하기2
연산3) 더하기1

위의 연산을 차례대로 실행하며 N을 찾는다...
음..

개선)
if *3을 해서 N보다 작다면 *3을 한다.
if *2를 해서 N보다 작다면 *2를 한다
else +1을 한다

=> 메모리 초과 났다.

아이디어2)
그냥 숫자를 만들어나가지 않고 줄여나가는 식으로 했다.
=> 시간 초과

아이디어3)
DP - 메모이제이션
=> 메모리초과

아이디어4)
메모이제이션의 메모리 초과 이유가 재귀 때문이라 생각..
dp - 타뷸레이션
=>성공!

[시간복잡도]
아이디어4)
배열 한 번만 훑으므로 O(n)


[실수]
solve(n):
    sum = 0
    for i in range(0, n):
        sum += n

이런 식으로 for 문 루프 안에서 i에 관한 내용이 아니라 n에 관한 내용을 작성하였다...

[검색]
재귀 리미트 해제
타뷸레이션 작성법

[개선/추가사항]
재귀 함수 만들 때 리턴 결과 먼저 생각해두고, 이를 간단히 활용하도록 만들자.

solve(1)부터 시작해서 정답이 되면, 리턴한다!!
이런 느낌보다는, 

solve(n)을 주면 그 안에서 solve(n-1) 따위를 이용하여 solve(n)을 해결하도록..

"""

global N
global min_count

def solve(num: int, count: int):
    # 메모리초과
    global N

    global min_count

    if num == N:
        min_count = min(min_count, count)
        return

    count+= 1

    plus = True
    if num * 3 <= N:
        plus = False
        solve(num * 3, count)
    if num * 2 <= N:
        plus = False
        solve(num * 2, count)
    if plus:
        solve(num + 1, count)

    return

def solve2(num: int, count: int):
    # 시간초과
    global min_count
    if num == 1:
        min_count = min(min_count, count)
        return
    count+= 1
    if (num % 3 == 0):
        solve2(num // 3, count)
    if (num % 2 == 0):
        solve2(num // 2, count)
    
    solve2(num-1, count)
    return


from collections import defaultdict
global d # dictionary
d = defaultdict(int)
global arr

# 리턴결과: n을 만드는데의 연산 횟수의 최솟값
def solve3(n) -> int:
    # DP -> 결과값을 딕셔너리에 저장해두자 (메모이제이션)
    # n을 만드는 연산 횟수의 최솟값은 다음 3가지 중 하나
    # 1) solve(n//3) + 1
    # 2) solve(n//2) + 1
    # 3) solve(n-1) + 1

    # => 메모리 초과
    if n == 1:
        return 0

    if (arr[n] != 0):
        return d[n]
    
    a = b = 9999999
    if (n % 3 == 0):
        a = solve3(n//3)
    if (n % 2 == 0):
        b = solve3(n//2)
    c = solve3(n - 1)

    ans = min(a, b, c) + 1
    arr[n] = ans
    return ans

def solve4(n) -> int:
    # 타뷸레이션으로 풀이
    # DP -> 결과값을 딕셔너리에 저장해두자
    # n을 만드는 최솟값은 다음 3가지 중 하나
    # 1) solve(n//3) + 1
    # 2) solve(n//2) + 1
    # 3) solve(n-1) + 1

    # 실수
    # N+1로 하니까 인덱스 오류가 났다.. 뭐임..
    # 아직 N은 초기화가 안 된 상태라서 그렇다!! 전역변수 사용시 주의...
    # n+1로 바꾸어 주었다.
    arr = [0 for _ in range(n+1)]
    arr[1] = 0
    arr[2] = 1
    arr[3] = 1
    
    for i in range(4, n+1):
         # 실수: i//3으로 해야 하는데 n//3으로 하는 등 i가 아니라 n에 대해 처리
        a = b = 99999999
        
        if (i % 3 == 0):
            a = arr[i//3]
        if (i % 2 == 0):
            b = arr[i//2]
        c = arr[i - 1]

        arr[i] = min(a, b, c) + 1
        
    return arr[n]


import sys
input = sys.stdin.readline

# recursive error
sys.setrecursionlimit(2000000)

N = int(input())
#실수: 초기값을 0으로 줬다..10.
min_count = 9999999
num = 1
# solve1(num, 0)
# solve2(num, 0)
# print(min_count)

# arr = [0 for _ in range(N+1)]
# answer = solve3(N)

answer = solve4(N)
print(answer)
