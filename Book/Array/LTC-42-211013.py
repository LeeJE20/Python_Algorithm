"""
https://leetcode.com/problems/trapping-rain-water/
42. Trapping Rain Water

난이도: Hard
"""

"""
시작: 21.10.13 11:06
끝: 
성공: 

메모리:  KB
시간:   ms

[아이디어]
투포인터

가장 높은 막대가 반드시 존재하게 됨.
양쪽 끝에서 가장 높은 막대를 향해 포인터가 이동.

투 포인터가 만날 때까지 양쪽에서 다음 과정 반복
투 포인터는 가장 높은 막대에서 만남

가장 높은 막대를 향해 양 방향에서 포인터 이동
지금까지의 두번쨰로 높은 막대, 가장 높은 막대가 있으면 2번 막대 높이에 맞게 물이 채워짐
-> 지금까지의 가장 높은 막대 보다 
    낮은 막대들에 대해서는 높은 막대 높이에 찰 만큼 물 넣고
    더 높은 막대 나오면 지금까지의 가장 높은 막대 update




[시간복잡도]



[실수]



[검색]



[개선/추가사항]

"""

# 21.10.06 11:59
class Solution:
    # 풀이1: 투 포인터를 최대로 이동
    # 어딘가에는 있을 가장 높은 height를 향해서 왼쪽, 오른쪽 포인터가 다가감
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        volume = 0

        # 왼쪽, 오른쪽 인덱스
        left, right = 0, len(height)-1
        # 왼쪽 최대의 height값, 오른쪽 최대의 height값
        left_max, right_max = height[left], height[right]



        while(right > left):
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])

            # 높이가 낮은 쪽의 포인터를 높은 쪽을 향해 이동시킴
            if left_max<= right_max:
                left += 1
                # 현재 max보다 작은 높이면 물 담김
                if height[left] < left_max:
                    volume += (left_max - height[left])
            else:
                right -= 1
                # 현재 max보다 작은 높이면 물 담김
                if height[right] < right_max:
                    volume += (right_max - height[right])

        return volume
            
            
            
            
# Runtime: 68 ms, faster than 90.55%
# Memory Usage: 15.5 MB, less than 86.21%
class Solution:
    def trap(self, height: list[int]) -> int:
    
        
        left, right = 0, len(height) -1
        left_max, right_max = height[left], height[right]

        volume = 0
        # 투 포인터가 만날 때까지 양쪽에서 다음 과정 반복
        # 투 포인터는 가장 높은 막대에서 만남
        while left < right:
            # 가장 높은 막대를 향해 양 방향에서 포인터 이동

            # 지금까지의 두번쨰로 높은 막대, 가장 높은 막대가 있으면 2번 막대 높이에 맞게 물이 채워짐
            # -> 지금까지의 가장 높은 막대 보다 
            #     낮은 막대들에 대해서는 높은 막대 높이에 찰 만큼 물 넣고
            #     더 높은 막대 나오면 지금까지의 가장 높은 막대 update
            if left_max <= right_max:
                left += 1
                if height[left] < left_max:
                    volume += (left_max - height[left])
                else:
                    left_max = height[left]
                # left_max = max(left_max, height[left])
            else: 
                right -= 1
                if height[right] < right_max:
                    volume += (right_max - height[right])
                else:
                    right_max = height[right]
        return volume


"""
스택

21.12.29 12:30 시작
22.01.05 10:45 종료

91 ms, faster than 27.36%
15.6 MB, less than 85.54% 
"""
h = 0
idx = 1

class Solution3:
    def trap(self, height: list[int]) -> int:
        rain = 0
        s = []
        index = 0
        # 높이, 인덱스를 스택에 넣는다.
        s.append((height[index], index))
        index += 1
        while (index < len(height)):
            # stack의 높이와 과 비교해서 현재값이 같거나 작으면 스택에 넣는다.
            if s[-1][h] >= height[index]:
                s.append((height[index], index))
                index += 1
                continue
            else:
                while True:
                    # stack과 현재값을 비교해서 크면 스택을 뺀다. -> 스택 low값
                    stack_low = s.pop()
                    # stack이 비었다면 현재값 추가 이후 종료
                    if not s:
                        s.append((height[index], index))
                        break
                    # 스택low값보다 큰 값이 stack에서 나올때까지 pop 반복 -> 스택high값
                    while (s and (s[-1][h] <= stack_low[h])):
                        s.pop()
                    if not s:
                        s.append((height[index], index))
                        break
                    stack_high = s[-1]
                    # 스택 high는 아직 pop하지 않은 상태가 된다.

                    # 빗물 계산
                    # 가로로 쌓는 느낌
                    # (min(스택high높이, 현재 높이)-스택low 높이) * (현재 idx - stack high 높이 idx -1)
                    rain += (min(stack_high[h], height[index]) - stack_low[h]) * (index - stack_high[idx] - 1)

                    # 만약 스택 high >= 현재높이라면, 스택에 현재 높이 추가
                    if stack_high[h] >= height[index]:
                        s.append((height[index], index))
                        index += 1
                        break
                    # 만약 스택 high높이 < 현재 높이라면, 위 과정 반복
        return rain



sol = Solution3()
test = (
    [[3, 1, 1, 4], 4],
    [[1, 1, 1, 3], 0],
    [[5, 2, 1, 5], 7],
    [[5, 4, 2, 1, 3, 5], 10],
    [[4, 1, 3, 4], 4]
)
            
for step, (data, ans) in enumerate(test):
    print(f"step: {step}, try: {sol.trap(data)}, ans = {ans}, {sol.trap(data)==ans}")