"""
https://www.acmicpc.net/problem/1697

숨바꼭질 

난이도: 실버 1

나중에 다시 풀자!!

시작: 21.06.02 22:31
끝: 21.06.02 23: 21
성공: 

메모리: 33196 KB
시간:  164 ms

[아이디어]
1. 브루투포스 -> 시간이 오래 걸릴 것.
비슷한 문제 푼 적이 있다... 수학문제였는데..

한 칸 이동하는 것은 그냥 +4 이런 식으로 했다.

흠,,


수빈이의 위치가 더 작다면: 무조건 -1로 한칸씩 이동해야 한다.

2. https://velog.io/@ember/DP-%EB%B0%B1%EC%A4%80-1463-1%EB%A1%9C-%EB%A7%8C%EB%93%A4%EA%B8%B0#1-%EC%A0%91%EA%B7%BC%EB%B2%95-2
이 문제랑 비슷한 것 같기도...
DP로 해볼까...

solve(n) 리턴 값: 수빈이가 n의 위치에 있을 때, 동생을 찾을 수 있는 가장 빠른 시간
solve(n) = min(solve(n-1), solve(n+1), solve(n/2)) + 1

근데 이 문제는 수빈이 위치가 동생보다 커질 수도 있어서 DP는 어렵겠다. n을 계산하려면 n+1도 필요하고, n+2도 필요하고.. 영원히 계산할 수는 없다.

3. 잘 모르겠어서 알고리즘 분류를 보았더니 너비우선 탐색이 있었다...
시간초과 날 것 같은데 되나?
일단 해보자..
시간: 22: 53


[시간복잡도]
너비우선탐색


[실수]
0. bfs랑 브루트포스랑 잘 구분을 못 한다.
    하나씩 다 해보는 건 그냥 다 브루트포스처럼 보인다...
    실수 방지: 브루트포스 느낌이 나면 그래프 문제인지 한번 더 생각해보자.

1. visited를 만들어 이미 갔던 곳은 다시 안 가게 해야 한다.
    실수 방지: 그래프 문제를 풀 때의 루틴을 어디 적어둬야겠다.

2. deque를 queue로 쓸 때는 popleft를 해야 앞에서 나온다.
    실수 방지: 변수 이름을 큐로 사용할 때는 q_deque로 만들어두자 (스택일때는 s_deque)

3. 실수: 범위 체크를 먼저 해야 인덱스 에러가 안 난다.
        if (now - 1 >= 0 and  visited[now - 1] == 0 ):
        이런 부분에서 visited 배열을 먼저 체크하면 인덱스 오류가 생긴다.




[검색]



[개선/추가사항]



[고수풀이]
링크: https://www.acmicpc.net/source/18296168

메모리: 29284 KB
시간:  56 ms


접근법:
dp로 풀었다!
나는 DP가 안 될 것 같았는데...

홀수와 짝수로 나눠서 
k가 홀수이면 걸어오게 하고, k가 짝수이면 순간이동을 하게 했다.
괜찮네,,

근데 접근법을 잘 모르겠다.
짝수일 떄 min(k-n) 이게 왜 나오지...

홀수면: 
    최소 횟수는 min(k-1에서 걸어오는 방법, k+1에서 걸어오는 방법) + 1
K가 짝수면:
    최소 횟수는 min(k에서 N까지 걸어오는 방법(한 칸씩 온다.), k//2에서 순간이동하는 방법)



배울 점: 


코드
def c(n,k):
    if n>=k:
        return n-k
    elif k == 1:
        return 1
    elif k%2: # 홀수면
        return 1+min(c(n,k-1),c(n,k+1))
    else: # 짝수면
        return min(k-n, 1+c(n,k//2))
    
n, k = map(int,input().split())
print(c(n,k))


"""


import collections
import sys
input = sys.stdin.readline

# 수빈이의 위치 N, 동생의 위치 K
N, K = map(int, input().split())

q = collections.deque()


count = -1

if (K <= N):
    count = N - K
    K = N
else:
    q. append(N)

now = N  # 현재 위치

# print(q.pop())


# 실수: visited를 만들어 이미 갔던 곳은 다시 안 가게 해야 한다.
visited = [0] * 100001
visited[now] = 1
while (now != K):
    count += 1
    for _ in range(len(q)):
        # 실수: popleft를 해야 앞에서 나온다.
        now = q.popleft()
        # print(now)
        if (now == K):
            # print(now)
            # print(f"K = {K}")
            break

        # q.append(now-1)
        # q.append(now+1)
        # q.append(now * 2)5


        # 실수: 범위 체크를 먼저 해야 인덱스 에러가 안 난다.
        if (now - 1 >= 0 and  visited[now - 1] == 0 ):
            q.append(now - 1)
            visited[now - 1] = 1

        if (now + 1 <= 100000 and visited[now + 1] == 0):
            q.append(now + 1)
            visited[now + 1] = 1
        if (now * 2 <= 100000 and visited[now * 2] == 0):
            q.append(now * 2)
            visited[now * 2] = 1


print(count)
