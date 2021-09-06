"""
https://leetcode.com/problems/reconstruct-itinerary/

332. Reconstruct Itinerary

난이도: medium

시작: 21.08.25 22:28
끝: 21.08.25 23:03
성공: wrong

메모리: 
시간: 


[아이디어]
dfs


[시간복잡도]
전부 훑어봐야하므로 O(노드 개수)


[실수]


"""

import collections

# 시도 1
# 재귀 깊이 범위 초과
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        # 단어순 순회-> 정렬
        for frm, to in sorted(tickets):
            graph[frm].append(to)

        path = []
        # 단어순 조회
        def dfs(now):
            # if not graph[now]:
            #     # path.append(now)
            #     return
            
            for to in graph[now]:
                dfs(to)
            
            path.append(now)
            return

        dfs("JFK")
        return path[::-1]


# 시도 2
# 고친점: 그래프에서 방문한 노드는 삭제했다
# Wrong Answer
# Details 
# Input
# [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# Output
# ["JFK","KUL"]
# Expected
# ["JFK","NRT","JFK","KUL"]

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        # 단어순 순회-> 정렬
        for frm, to in sorted(tickets, reverse = True):
            graph[frm].append(to)

        path = []
        # 단어순 조회
        def dfs(now):
            # if not graph[now]:
            #     # path.append(now)
            #     return
            
            for _ in graph[now]:
                # 그래프에서 방문한 노드 삭제
                to = graph[now].pop()
                dfs(to)
            
            path.append(now)
            return

        dfs("JFK")
        return path[::-1]

# 시도 3
# IndexError: pop from empty list
#     to = graph[now].pop()
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        # 단어순 순회-> 정렬
        for frm, to in sorted(tickets, reverse = True):
            graph[frm].append(to)

        path = []
        # 단어순 조회
        def dfs(now):
            # if not graph[now]:
            #     # path.append(now)
            #     return
            
            # 반복을 덜 하는 것 같아서 횟수로 변환
            # 실수: len을 안 붙임

            # for _ in range(graph[now]):
            for _ in range(len(graph[now])):
                # 그래프에서 방문한 노드 삭제
                to = graph[now].pop()
                dfs(to)
            
            path.append(now)
            return

        dfs("JFK")
        return path[::-1]


# 시도 4
# 기저 조건
# 틀림
# 정답과 비교: 루프에 while을 썼다...
# dfs 도중에 현재 노드에 또 접근할 수 있으므로 for로 하면 엉키게 된다.
# a-> b, c / b->a인 경우
# 1. a에서 for루프 2번 돌게 되어 있음 (b방문)
# 2. b-> a로 감
# 3. a에서 for루프 1번 돌기 (c 방문)
# 4. 1에서 a의 2번째 루프가 남았는데, 이제 방문할 노드가 없음
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        # 단어순 순회-> 정렬
        for frm, to in sorted(tickets, reverse = True):
            graph[frm].append(to)

        path = []
        # 단어순 조회
        def dfs(now):
            if not graph[now]:
                # path.append(now)
                return
            
            # 반복을 덜 하는 것 같아서 횟수로 변환
            # 실수: len을 안 붙임

            # for _ in range(graph[now]):
            for _ in range(len(graph[now])):
                # 그래프에서 방문한 노드 삭제
                to = graph[now].pop()
                dfs(to)
            
            path.append(now)
            return

        dfs("JFK")
        return path[::-1]