# https://leetcode.com/problems/course-schedule/
# 21.08.20

"""내 아이디어
위상정렬 문제

1->2

사이클이 없어야 한다.
-> 이미 탐색한 노드로 향하는 간선이 없어야 한다.

탐색한 노드 체크해두고, 이미 탐색한 노드를 또 찾는 경우가 있는지 확인

"""


""" 문법

graph = defaultdict(list) 객체를 이터레이션

for x in graph: # 런타임에러: 이터레이션 도중 딕셔너리 변경
    - 존재하지 않는 키를 조회할 때 오류를 내지 않기 위해 디폴트를 생성하기 때문
=> 해결방안
for x in list(graph)

"""

import collections
# 풀이1: DFS로 순환 구조 판별
# 그래프가 순환 구조인지 판별하는 문제
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for x, y in prerequistes:
            graph[x].append(y)

        # 이미 방문했던 노드
        # 이미 방문했던 곳을 중복 방문하면 순환구조
        traced = set()

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)

            return True

        
        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False


        return True


# 풀이2: 가지치기를 이용한 최적화
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        # 그래프 구성
        for x, y in prerequisites:
            graph[x].append(y)


        traced = set()
        visited = set()

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False
            # 이미 방문했던 노드이면 True
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            # 탐색 종료 후 순환 노드 삭제
            traced.remove(i)

            # 탐색 종료 후 방문 노드 추가
            visited.add(i)

            return True

        # 순환 구조 판별
        for x in list(graph):
            if not dfs(x):
                return False

        return True