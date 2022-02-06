# https://leetcode.com/problems/trapping-rain-water/
# 21.10.06/

# 내 풀이
# 21.10.06 11:59
# 10/06/2021 12:44	Wrong Answer
# 스택 사용
class Solution:
    def trap(self, height: List[int]) -> int:
        # stack
        # index, height 순서
        s = []

        water = 0
        for i, h in enumerate(height):

            print(f"i, h = {i}, {h}")
            if (len(s) == 0) and h == 0:
                continue
            if h > 0 and (len(s) == 0) or (len(s) > 0 and s[-1][1] > h):
                s.append([i, h])
                # print(s)
                continue

            # top = s[-1][1]

            # if top > h:
            #     s.append([i, h])
            #     continue

            # 물이 차는 경우

            while (len(s) > 1 and s[-1][1] < h):
                print(s, h)
                water += (i - s[-1][0])
                print(f"water: {water}")
                s.pop()
            if (len(s) == 1 and s[-1][1] <= h):
                s.pop()
                s.append([i, h])

        return water


# 풀이1: 투 포인터를 최대로 이동
# 어딘가에는 있을 가장 높은 height를 향해서 왼쪽, 오른쪽 포인터가 다가감
def trap(self, height: List[int]) -> int:
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

        # # 내가 쓴 부분
        # # 높이가 낮은 쪽의 포인터를 높은 쪽을 향해 이동시킴
        # if left_max<= right_max:
        #     left += 1
        #     # 현재 max보다 작은 높이면 물 담김
        #     if height[left] < left_max:
        #         volume += (left_max - height[left])
        # else:
        #     right -= 1
        #     # 현재 max보다 작은 높이면 물 담김
        #     if height[right] < right_max:
        #         volume += (right_max - height[right])

        # 교재
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume



# 풀이2: 스택 쌓기
def trap(self, height: List[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우 (높이가 높아지는 경우)
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다
            top = stack.pop()

            # 스택 비었으면 종료
            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        # 스택에는 인덱스만 저장하고, height는 list에서 읽어서 사용
        stack.append(i)
    return volume