"""
https://www.acmicpc.net/problem/2447


시작: 21.05.16 12:00
끝: 21.05.16 12:19
성공: correct

[아이디어]
2차원 리스트를 기본값 ' '(공백)으로 만들어두고,,, 분할정복으로 하나씩 훑어간다.
구역은 9 구역으로 나눈다.

1 2 3
4 5 6
7 8 9

각 구역은 가운데 부분과 나머지 부분으로 나뉜다.

기저: 
크기가 1이다.
가운데 부분: 공백으로 가만히 냅둔다.


solve():
    # 5 부분 처리 (아무것도 안 하면 됨)
    # 나머지 부분: 재귀

[시간복잡도]
가운데 부분 빼고 모든 판을 읽어야 하므로 O(n^2)


[실수]


[검색]
    2차원 리스트 만들기
    rr = [[' ' for j in range(N)] for i in range(N)] # 바깥 for문을 뒤에

    2차원 리스트 쓰기
    for i in arr:
        for j in i:
            print(j, end='')
        print()
        
[개선/추가사항]

[느낀점]
이 문제는 실버1인데 너무 쉬웠다.
라고 생각했으나...
고수의 풀이를 보니 좀 더 효율적인 코드로 만든다면 실버1일만 하다.

"""

global arr

def solve(size: int, x: int, y: int) -> None:
    global arr

    if size == 1:
        arr[x][y] = '*'
        return
    
    next_size = int(size/3)

    solve(next_size, x, y);
    solve(next_size, x + next_size, y);
    solve(next_size, x + next_size * 2, y);

    solve(next_size, x, y + next_size);
    solve(next_size, x + next_size * 2, y + next_size);

    solve(next_size, x, y + next_size * 2);
    solve(next_size, x + next_size, y + next_size * 2);
    solve(next_size, x + next_size * 2, y + next_size * 2);


import sys
input = sys.stdin.readline

N = int(input())
arr = [[' ' for j in range(N)] for i in range(N)] # 바깥 for문을 뒤에
solve(N, 0, 0)

for i in arr:
    for j in i:
        print(j, end='')
    print()