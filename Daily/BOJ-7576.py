"""
https://www.acmicpc.net/problem/7576

토마토

난이도: 실버 1

시작: 21.05.30 14:17

쉬는시간: 14:45 ~ 20: 41
끝: 21.05.30 20:51

총 소요시간: 38분

성공: correct

메모리: 106836 KB
시간:  1804 ms

[아이디어]
bfs
테이블 읽어나가며 익은 토마토 위치를 전부 큐에 넣는다.
또한 익은 토마토 개수와, 빈칸의 개수를 센다
if not q: print -1
elif 익은 토마토 개수 + 빈칸 개수 == M*N : print 0
count = -1
while(q):
    count += 1
for len(q):
    cur_point
    q의 상, 하, 좌, 우가 0이면:
        q.push(상, 하, 좌, 우)

if all in list == print count
else: print -1

아이디어 끝: 14:23
소요시간: 6분


[시간복잡도]
인접리스트인 것 같다..
그러니 O(V+E)




[실수]
# 실수1: 도착했다고 표시를 안 함
    arr[y-1][x] = 1
    bfs는 도착했다고 표시를 해야 하는데, 빼먹었다...

    재발 방지: 음.. bfs의 관행을 더 잘 외워야겠다...


# 실수2: 모든 토마토가 익을 수 없는 경우 계산 안 함
    마지막에 ripe_tomate + no_tomate = M*N이어야 한다.

    재발 방지: 
        1. 문제 꼼꼼히 읽기
        2. 예외 조건 먼저 생각하기
            (특히 시작, 마지막 값 생각하기)
        3. 그 다음 일반 조건에 대한 구현 아이디어 생각하기



[검색]



[개선/추가사항]



[고수풀이]
링크: https://www.acmicpc.net/source/22461547

메모리: 98464 KB
시간:  1080 ms


접근법: 나랑 같다.


배울 점: 
    1. 나는 전부 배열에 저장하고 그걸 나중에 또 읽었는데, 
        고수는 저장하면서 읽는다.
    2. 나는 익은 토마토와 빈 칸의 개수를 모두 헤아렸는데,
        고수는 haveTo만 헤아린다.
        조건도 haveTo == 0이라면~~ 이런 식으로 진행한다.
        (나는 M*N을 또 연산해야 했다.)

        * 이런 식으로 해야 할 일의 개수를 0으로 줄여나가는 접근법을 배우자.

    3. 


코드
import sys
from collections import deque
input = sys.stdin.readline


def solve():
    m, n = map(int, input().split())
    tomato = []
    haveto = 0
    tmt = deque()
    for i in range(n):
        tomato.append(input().split())
        for j in range(m):
            if tomato[i][j] == '0':
                haveto += 1
            elif tomato[i][j] == '1':
                tmt.append((i, j))
    res = 0
    while tmt and haveto:
        l = len(tmt)
        for _ in range(l):
            x, y = tmt.popleft()
            if x > 0 and tomato[x-1][y] == '0':
                tomato[x-1][y] = 1
                tmt.append((x-1, y))
                haveto -= 1
            if y > 0 and tomato[x][y-1] == '0':
                tomato[x][y-1] = 1
                tmt.append((x, y-1))
                haveto -= 1
            if x < n-1 and tomato[x+1][y] == '0':
                tomato[x+1][y] = 1
                tmt.append((x+1, y))
                haveto -= 1
            if y < m-1 and tomato[x][y+1] == '0':
                tomato[x][y+1] = 1
                tmt.append((x, y+1))
                haveto -= 1
        res += 1
    if haveto:
        print(-1)
    else:
        print(res)


if __name__ == '__main__':
    solve()


"""
from collections import deque
import sys
input = sys.stdin.readline


M, N = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))


no_tomato = 0
ripe_tomato = 0
q = deque()
# 테이블 읽어나가며 익은 토마토 위치를 전부 큐에 넣는다.
# 또한 익은 토마토 개수와, 빈칸의 개수를 센다
for n in range(N):
    for m in range(M):
        if arr[n][m] == 1:  # 익은 토마토
            ripe_tomato += 1
            q.append([n, m])
        elif arr[n][m] == -1:  # 빈칸
            no_tomato += 1

if ripe_tomato == 0:
    print(-1)
elif ripe_tomato + no_tomato == M*N:
    print(0)
else:
    # print(q)
    count = -1
    while(q):
        count += 1
        # print('\n'.join(map(str, arr)))
        # print(f"len(q): {len(q)}")
        for i in range(len(q)):
            # print(f"~~~~~~~~~~~~~~~~i = {i}")
            y, x = q.popleft()
            # print(f"y, x = {y}, {x}")

    #         # q의 상, 하, 좌, 우가 0이면:
    #         #     q.push(상, 하, 좌, 우)
            if (y-1) >= 0 and arr[y-1][x] == 0:
                # 실수: 도착했다고 표시를 안 함
                arr[y-1][x] = 1
                # 실수: 모든 토마토가 익을 수 없는 경우 계산 안 함
                # 마지막에 ripe_tomate + no_tomate = M*N이어야 한다.
                ripe_tomato += 1
                q.append([y-1, x])
            if (y+1) < N and arr[y+1][x] == 0:
                arr[y+1][x] = 1
                ripe_tomato += 1
                q.append([y+1, x])
            if (x-1) >= 0 and arr[y][x-1] == 0:
                arr[y][x-1] = 1
                ripe_tomato += 1
                q.append([y, x-1])
            if (x+1) < M and arr[y][x+1] == 0:
                arr[y][x+1] = 1
                ripe_tomato += 1
                q.append([y, x+1])
    
    if ripe_tomato + no_tomato == M*N:
        print(count)
    else:
        print(-1)
