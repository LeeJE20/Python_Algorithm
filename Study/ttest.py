h = 0
idx = 1

class Solution:
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
                        index += 1
                        break
                    # 스택low값보다 큰 값이 stack에서 나올때까지 pop 반복 -> 스택high값
                    while (s[-1][h] <= stack_low[h]):
                        s.pop()
                        # stack이 비었다면 현재값 추가 이후 종료
                        if not s:
                            s.append((height[index], index))
                            index += 1
                            break
                    stack_high = s[-1]
                    # 스택 high는 아직 pop하지 않은 상태가 된다.

                    # 빗물 계산
                    # (min(스택high높이, 현재 높이)-스택low 높이) * (현재 idx - stack high 높이 idx -1)
                    tmp = ((min(stack_high[h], height[index]) - stack_low[h]) * (index - stack_high[idx] - 1))
                    rain += tmp
                    print(f"now : ({height[index]}, {index})")
                    print(f"low : {stack_low}")
                    print(f"high: {stack_high}")
                    print(f"rain: {rain}")
                    print()

                    # 만약 스택 high >= 현재높이라면, 스택에 현재 높이 추가
                    if stack_high[h] >= height[index]:
                        s.append((height[index], index))
                        index += 1
                        break
                    # 만약 스택 high높이 < 현재 높이라면, 위 과정 반복
        return rain


sol = Solution()
print(sol.trap([4, 3, 2, 1, 3, 4]))