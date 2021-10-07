# https://leetcode.com/problems/subsets/
# 21.08.18

"""아이디어
for i in range(1, len(nums)):
    result.append(combination(nums, i))
"""

# 내 풀이
from typing import List
import itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i in range(1, len(nums)+1):
            result+=list(map(list, itertools.combinations(nums, i)))
        return result


# 교재 풀이1: 트리의 모든 DFS 결과
def subsets(self, nums: List[int]) -> List[List[int]]:
    result = []

    def dfs(index, path):
        # 매번 결과 추가
        result.append(path)

        # 경로를 만들면서 DFS
        for i in range(index, len(nums)):
            dfs(i+1, path + [nums[i]])
    
    dfs(0, [])
    return result