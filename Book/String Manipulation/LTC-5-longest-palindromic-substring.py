# https://leetcode.com/problems/longest-palindromic-substring/
# 21.09.23



# 풀이1: 중앙을 중심으로 확장하는 풀이

# LCS(최장 공통 부분 문자열, Longest Common Substring)문제
# DP로 풀 수 있는 전형적 문제

# 이 문제는 DP 풀이가 직관적으로 어렵고, 느림



# 따라서 투 포인터가 중앙을 중심으로 확장하는 형태로 풀이

# 팰린드롬 판별만 하면 됨
# 매칭이 될 때 중앙을 중심으로 점점 확장해 나가면서 가장 긴 팰린드롬 판별

# 팰린드롬은 bb처럼 짝수일수도, bab처럼 홀수일수도 있음→ 처음 시작이 2칸 or 3칸
# 2칸, 3칸으로 구성된 투 포인터가 앞으로 전진
# 이때 윈도우에 들어온 문자열이 팰린드롬인 경우, 투 포인터 확장
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 팰린드롬 판별 및 투 포인터 확장
        def expand(left: int, right: int) -> str:
            while left>=0 and right<len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]


        # 예외처리
        if len(s) < 2 or s == s[::-1]:
            return s

        # 슬라이딩 윈도우가 문자열 처음부터 끝까지 우측으로 이동
        for i in range(0, len(s) - 1):
            result = max(result, 
                        expand(i, i+1), 
                        expand(i, i+2), 
                        key = len)

        return result