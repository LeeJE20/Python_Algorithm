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