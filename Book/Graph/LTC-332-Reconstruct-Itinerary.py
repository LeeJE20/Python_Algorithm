# https://leetcode.com/problems/reconstruct-itinerary/
# 21.08.19 10:48

"""
1. 입력을 사전순으로 정렬
2. JFK에서 출발하는 깊이우선탐색
"""

# 풀이1: DFS로 일정 그래프 구성


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 그래프 구성
        graph = collections.defaultdict(list)

        # for a, b in tickets:
        #     graph[a].append(b)
        # # 정렬 -> 어휘순으로 방문할 수 있게
        # for a in graph:
        #     graph[a].sort()

        # 그래프 순서대로 구성
        # tickets를 정렬한 다음 딕셔너리에 넣기
        for a, b in sorted(tickets):
            graph[a].append(b)


        route = []
        def dfs(a):
            while graph[a]:
                # 첫 번째 값을 읽어 어휘 순 방문
                dfs(graph[a].pop(0))
            # 더이상 갈 곳이 없으면 append
            # 즉, 도착지점이란 뜻
            route.append(a)

        dfs('JFK')
        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]


# 풀이2: 스택 연산으로 큐 연산 최적화 시도
# pop(1) 대신 pop() 연산 사용
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        # 그래프를 뒤집어서 역순으로 구성
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        route = []
        def dfs(a):
            # 마지막 값을 읽어 어휘 순 방문
            while graph[a]:
                dfs(graph[a].pop(0))
            # 더이상 갈 곳이 없으면 append
            # 즉, 도착지점이란 뜻
            route.append(a)

        dfs('JFK')
        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]


# 풀이3: 일정 그래프 반복
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # 그래프 구성
        graph = collections.defaultdict(list)


        # 그래프 순서대로 구성
        # tickets를 정렬한 다음 딕셔너리에 넣기
        for a, b in sorted(tickets):
            graph[a].append(b)


        route, stack = [], ['JFK']
        while stack:
            # 반복으로 스택을 구성하되 막히는 부분에서 풀어내는 처리
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop())


        # 다시 뒤집어 어휘 순 결과로
        return route[::-1]