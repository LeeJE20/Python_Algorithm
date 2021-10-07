"""
https://leetcode.com/problems/course-schedule/

207. Course Schedule

난이도: medium

시작: 21.08.23 20:26
끝: 21.08.23 20:51
성공: worng: Time Limit Exceeded

메모리: 
시간: Time Limit Exceeded


=> 교재 보고 dfs의 파라미터 적게 개선
성공: correct
메모리: 17.1 MB, less than 39.88%
시간: 172 ms, faster than 11.37%

[아이디어]
사이클 없게...


[시간복잡도]



[실수]


"""

# import collections

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         # 그래프 구축
#         graph = collections.defaultdict(list)

#         # y를 끝내야 x를 할 수 있다
#         for x, y in prerequisites:
#             graph[y].append(x)

        
#         # dfs 하면서 사이클 찾기
#         def dfs(path, now, checked):
#             if now in path:
#                 return False
#             # 사이클 없는 노드는 통과
#             if now in checked:
#                 return True
#             path.append(now)
#             for child in graph[now]:
#                 if dfs(path, child, checked):
#                     pass
#                     # checked.append(child)
#                 else: 
#                     return False
#             checked.append(now)
#             path.pop()

#             return True

#         # graph.keys가 아니라 graph.keys()
#         for i in list(graph.keys()):
#             if not dfs([], i, []):
#                 return False

#         return True
        


# 교재 보고 dfs 파라미터를 하나만 넘기게 수정
# import collections

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         # 그래프 구축
#         graph = collections.defaultdict(list)

#         # y를 끝내야 x를 할 수 있다
#         for x, y in prerequisites:
#             graph[y].append(x)

#         path = []
#         checked = []
        
#         # dfs 하면서 사이클 찾기
#         def dfs(now):
#             if now in path:
#                 return False
#             # 사이클 없는 노드는 통과
#             if now in checked:
#                 return True
#             path.append(now)
#             for child in graph[now]:
#                 if dfs( child):
#                     pass
#                     # checked.append(child)
#                 else: 
#                     return False
#             checked.append(now)
#             path.pop()

#             return True

#         # graph.keys가 아니라 graph.keys()
#         for i in list(graph.keys()):
#             if not dfs( i):
#                 return False

#         return True




# 리스트 대신 set 사용하게 수정
# SET은 IN 연산이 O(1)이라서 더 빠르다.
# Runtime: 96 ms, faster than 75.24% 
# Memory Usage: 17.1 MB, less than 39.88%
import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 그래프 구축
        graph = collections.defaultdict(list)

        # y를 끝내야 x를 할 수 있다
        for x, y in prerequisites:
            graph[y].append(x)

        path = set()
        checked = set()
        
        # dfs 하면서 사이클 찾기
        def dfs(now):
            if now in path:
                return False
            # 사이클 없는 노드는 통과
            if now in checked:
                return True
            path.add(now)
            for child in graph[now]:
                if dfs( child):
                    pass
                    # checked.append(child)
                else: 
                    return False
            checked.add(now)
            path.remove(now)
            
            return True

        # graph.keys가 아니라 graph.keys()
        for i in list(graph.keys()):
            if not dfs( i):
                return False

        return True