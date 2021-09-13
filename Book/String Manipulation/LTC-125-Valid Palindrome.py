# https://leetcode.com/problems/valid-palindrome/
# 21.09.10

# 풀이1: 리스트로 변환
def isPalindrome(self, s: str) -> bool:
    # 대소문자 구별 x, 영문자, 숫자만을 대상
    # 이 부분에 대한 전처리
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True



# 풀이2: 데크 자료형을 이용한 최적화
import collections

def isPalindrome(self, s: str) -> bool:
    # 자료형 데크로 선언
    strs: Deque = collections.deque()

    # 대소문자 구별 x, 영문자, 숫자만을 대상
    # 이 부분에 대한 전처리
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.popleft() != strs.pop():
            return False

    return True


# 풀이3: 슬라이싱 사용
def isPalindrome(self, s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s==s[::-1] # 슬라이싱
    