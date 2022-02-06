"""
스택 이용

1. 탐색 시작 노드를 스택에 삽입하고 방문 처리
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면, 
    그 인접노드를 스택에 넣고, 
    방문처리

    방문하지 않은 인접 노드가 없으면,
    스택에서 최상단 노드 꺼내기
3. 2의 과정을 반복

"""

# 재귀
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)