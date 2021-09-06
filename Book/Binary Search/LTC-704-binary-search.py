# 내 풀이
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # print(nums)
        # print(target)
        left = 0
        right = len(nums)
        mid = (right - left) // 2
        # print(f"l, r, m = {left}, {right}, {mid}")
        
        while (nums[mid] != target):
            # if (right == left):
            #     return -1
            if (nums[mid] < target):
                left = mid + 1
            else:
                right = mid

            # 실수: 
            # while에서 인덱스 오류나서 위치 바꿈
            if (right == left):
                return -1
            
            # 실수: mid를 left에서 더 나아간 크기가 아닌, 그냥 right와 left사이의 절반 크기로 지정해버림
            # mid = (right - left) // 2
            mid = left + (right - left) // 2
            
            # print(f"l, r, m = {left}, {right}, {mid}")
            
        return mid




# 교재 풀이1: 재귀 풀이
def search(self, nums:List[int], target: int) -> int:
    def binary_search(left, right):
        if left <= right:
            # 내 풀이랑 비교: 오우.. right - left로 가운데를 구하지 않아도 되네
            # 참고: 다른 언어는 left+right 부분에서 오버플로우가 날 수 있다. 
            #       따라서 left + (right - left) // 2 로 해야 함
            mid = (left + right) // 2

            if nums[mid] < target:
                return binary_search(mid+1, right)
            elif nums[mid] > target:
                return binary_search(left, mid - 1)
            else:
                return mid


# 교재 풀이2: 반복 풀이
def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) -1

    # 비교: while문을 빠져나가면 자연스럽게 리턴 -1을 해도 되게 해뒀다!!
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid

    return -1


# 교재 풀이3: 이진 검색 모듈
def search(self, nums: List[int], target: int) -> int:
    index = bisect.bisect_left(nums, target)

    if index < len(nums) and nums[index] == target:
        return index
    else:
        return -1


# 교재 풀이4: 이진 검색을 사용하지 않는 index 풀이
# 비권장 (이진 검색 아님)
def search(self, nums: List[int], target: int) -> int:
    try: 
        return nums.index(target)
    except ValueError:
        return -1