# https://www.algospot.com/judge/problem/read/DICTIONARY
# 21.08.20

""" 내 아이디어
단어마다 뜯어서 순서 찾고
위상정렬: 사이클이 있는지 찾는다
(DAG인지 확인한다.)


dfs돌고 거꾸로 출력했을때 반복되는 것이 있는지 확인??
구현을 모르곘다.
"""

# 코드 28.2
# 고대어 사전 문제의 그래프를 생성

# 알파벳의 각 글자에 대한 인접 행렬 표현
# 간선 (i, j)는 알파벳 i가 j보다 앞에 나와야 함을 나타낸다.
adj = [[]]

# 주어진 단어들로부터 알파벳 간의 선후관계 그래프를 생성한다.
def make_graph(words: List[str]) -> None:
    adj = [[0 for _ in range(26)] for _ in range(26)]
    for j in range(1, len(words)):
        i = j-1
        length = min(len(words[i]), len(words[j]))

        # word[i]가 word[j] 앞에 오는 이유를 찾는다.
        for k in range(length):
            if (words[i][k] != words[j][k]):
                a:int = ord(words[i][k]) - ord('a')
                b:int = ord(words[j][k]) - ord('a')
                # 글자 a가 b보다 앞에 온다는 표시
                adj[a][b] = 1
                break



### 코드 28.3

# 깊이우선탐색→ dfs()가 종료하는 순서 기록→ 순서 뒤집기: 위상정렬
# 이 순서대로 정점을 배열하였을 때 오른쪽→ 왼쪽으로 가는 간선이 있으면 사이클 존재.

seen = []
order = []

def dfs(here: int):
    seen[here] = 1
    for there in range(len(adj)):
        if(adj[here][there] and not seen[there]):
            dfs(there)
    order.append(here)

# adj에 주어진 그래프를 위상정렬한 결과를 반환한다.
# 그래프가 DAG가 아니라면 빈 벡터를 반환한다.
def topological_sort() -> List[int]:
    m:int = len(adj)
    seen = [0 for _ in range(m)]
    order.clear()

    for i in range(m):
        if (not seen[i]):
            dfs(i)

    order.reverse()

    # 만약 그래프가 DAG가 아니라면 정렬 결과에 역방향 간선이 있다.
    for i in range(m):
        for j in range(i+1, m):
            # 정렬 결과 뒤쪽에 오는 것이 앞쪽에 오는 것보다 사전순으로 앞에 있다면
            if adj[order[j]][order[i]]:
                return []
    
    # 역방향 간선이 없는 경우라면 깊이 우선 탐색에서 얻은 순서 반환
    return order