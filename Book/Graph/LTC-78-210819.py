"""
https://leetcode.com/problems/subsets/

78. Subsets

난이도: medium

시작: 21.08.19 22:33
끝: 21.08.16 22:43
성공: correct

메모리: 14.5 MB, less than 53.24%
시간: 36 ms, faster than 52.55%


[아이디어]
combination을 중간중간 출력해준다.


[시간복잡도]



[실수]
# 실수: 범위 끝을 nums가 아니라 result로 함
# for i in range(start_idx, len(result)):
for i in range(start_idx, len(nums)):

변수 이름을 비슷한 다른 것으로 잘못 쓰는 실수를 많이 한다.
변수를 쓸 때 그것이 맞는지 생각하면서 코드를 짜야 한다.

"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(start_idx, picked):

            result.append(picked[:])

            # 실수: 범위 끝을 nums가 아니라 result로 함
            # for i in range(start_idx, len(result)):
            for i in range(start_idx, len(nums)):
                picked.append(nums[i])
                dfs(i+1, picked)
                picked.pop()

        dfs(0, [])

        return result


            