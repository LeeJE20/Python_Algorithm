# https://leetcode.com/problems/two-sum/
# 21.09.24

# 풀이1: 브루트 포스로 계산
# O(n^2) 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 풀이2: in을 이용한 탐색
# 타겟에서 첫 번째 값을 뺀 값 target-n이 존재하는지 탐색
# O(n^2) 이지만 in을 써서 더 빠름
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            complement = target - n
            
            if complement in nums[i + 1:]:
                retrun [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


# 풀이3: 첫 번째 수를 뺀 결과 키 조회
# O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]

# 풀이4: 조회 구조 개선
# O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        # 하나의 for 문으로 통합
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target - num], i]
            nums_map[num] = i


# 풀이 5: 투 포인터 이용 (틀린 풀이: 정렬 안 되어 있음)
# 투 포인터: 왼쪽 포인터와 오른쪽 포인터의 합이 
    # 타겟보다 크다면 오른쪽 포인터를 왼쪽으로,
    # 작다면 왼쪽포인터를 오른쪽으로 옮김
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) -1
        while not left == right:
            # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return [left, right]
            