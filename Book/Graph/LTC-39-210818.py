"""
https://leetcode.com/problems/combination-sum/

39. Combination Sum

난이도: Medium

시작: 21.08.18 11:06
끝: 21.08.18 11:17
성공: correct

메모리: 14.4 KB, beats 25.23 %
시간:   52 ms, beats 92.78 %

[아이디어]
candidates의 합이 target이 되는 경우? (중복조합)

result = []
def dfs(picked, can, sum):
    for i in range(can):
        now = can[i]
        if sum+now < target:
            dfs(picked+[now], can[i:], sum+now)
        elif sum+now == target:
            result.append(picked+[now])




[시간복잡도]
cSum이 target을 넘을 때 끝이 난다.
O(?)


[실수]
 

[검색]



[개선/추가사항]



"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(picked, can, sum):
            for i in range(len(can)):
                now = can[i]
                if sum+now < target:
                    dfs(picked+[now], can[i:], sum+now)
                elif sum+now == target:
                    result.append(picked+[now])
        dfs([], candidates, 0)
        return result