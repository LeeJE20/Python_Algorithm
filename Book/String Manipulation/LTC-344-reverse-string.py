# https://leetcode.com/problems/reverse-string/
# 21.09.14

# 풀이1: 투 포인터를 이용한 스왑
def reverseString(self, s:List[str]) -> None:
    left, right = 0, len(s)-1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# 풀이2: 파이썬다운 방식
def reverseString(self, s:List[str]) -> None:
    s.reverse()

# 풀이3: 파이썬다운 방식2
def reverseString(self, s:List[str]) -> None:
    # 공간복잡도 제한때문에 안된다
    # s = s[::-1]
    s[:] = s[::-1]
