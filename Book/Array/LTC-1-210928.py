"""
https://leetcode.com/problems/two-sum/

1. Two Sum

난이도: Easy

시작: 21.10.05 10:42
끝: 21.05.11 12:13
성공: 

메모리:  KB
시간:   ms

[아이디어]



[시간복잡도]



[실수]



[검색]



[개선/추가사항]




"""
# Runtime: 5144 ms, faster than 11.63%
# Memory Usage: 14.7 MB, less than 92.40%



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 실수: enumerate는 인덱스, item 순서로 반환된다.
        for i, n in enumerate(nums[:-1]):

            # 배열을 잘라서 넣어주면 잘린부분의 첫 번쨰 인덱스가 0이 된다.
            # for j, m in enumerate(nums[i+1:]):
            for j in range(i+1, len(nums)):
                if nums[j] == target - n:
                    return [i, j]


# 딕셔너리로 만들기
# Runtime: 129 ms, faster than 40.14%
import collections
# 실수: nums에 같은 숫자가 들어있을 수 있음

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = collections.defaultdict(list)
        for i, n in enumerate(nums):
            d[n].append(i)
        for n in nums:
            # 실수: 4=2+2처럼 같은 숫자가 반복되는 경우 배제해야함
            if (target-n) != n and len(d[target-n]) > 0:
                return [d[n][0], d[target-n][0]]
            elif((target-n) == n and len(d[target-n]) > 1):
                return [d[n][0], d[target-n][1]]
