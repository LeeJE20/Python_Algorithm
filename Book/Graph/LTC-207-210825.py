"""
https://leetcode.com/problems/course-schedule/

207. Course Schedule

난이도: medium

시작: 21.08.25 23:08
끝: 21.08.25 23:23
성공: correct

메모리: 17 MB, less than 39.93%
시간: 100 ms, faster than 52.89%

[아이디어]
사이클 없게...


[시간복잡도]



[실수]
그래프 변경 에러가 나와서 그래프 key 값을 리스트 객체로 만들고 루프 돌았다.

"""

import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for sec, fir in prerequisites:
            graph[fir].append(sec)

        traced = set()
        checked = set()

        def dfs(now):
            if now in traced:
                return False
            if now in checked:
                return True

            traced.add(now)
            for next in graph[now]:
                if not dfs(next):
                    return False
            traced.remove(now)
            checked.add(now)

            return True
        
        # 그래프 변경 에러
        # for i in [graph.keys()]:
        #     if not dfs(i):
        #         return False

        key = list(graph.keys())
        for i in key:
            if not dfs(i):
                return False

        return True
        
        
            