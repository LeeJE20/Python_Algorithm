"""
https://leetcode.com/problems/reconstruct-itinerary/

332. Reconstruct Itinerary

난이도: medium

시작: 21.08.16 22:30
끝: 21.08.16 22:42
성공: wrong

메모리: 14.7 MB, less than 59.00%
시간: 76 ms, faster than 83.08%


[아이디어]
dfs


[시간복잡도]
전부 훑어봐야하므로 O(노드 개수)


[실수]


"""

import collections

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for frm, to in sorted(tickets, reverse = True):
            graph[frm].append(to)
        
        route = []


        # def dfs(frm):
        #     for i in range(len(frm)):
        #         to = graph[frm].pop()
        #         dfs(to)
        # #이렇게 하면 한 장소가 2번 출발함
        #         route.append(frm)

        def dfs(frm):
            while graph[frm]:
                to = graph[frm].pop()
                dfs(to)
            route.append(frm)
        
        dfs("JFK")
        return route
            