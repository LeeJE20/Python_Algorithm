"""
https://leetcode.com/problems/longest-palindromic-substring/

5. Longest Palindromic Substring

난이도: Medium

시작: 21.09.24 10:50
끝: 21.09.24 11:26
성공: 테스트 2회, 제출 1회

메모리:  14.3 MB, less than 81.37%
시간:   992 ms, faster than 70.09%

[아이디어]
2개, 3개씩 슬라이딩해나간다.
슬라이딩 윈도우 안이 팰린드롬이면 윈도우 영역을 넓혀간다.


[시간복잡도]
O(n^2)



[실수]
result = max(result, another)에서 
result 객체를 초기화하지 않고 max안에 파라미터로 넣어서 오류 생김




[검색]



[개선/추가사항]




"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_palindrome(left, right):
            # s 인덱스 범위 벗어나는 경우
            if not (left >= 0 and right < len(s)):
                return ""

            # 양 옆으로 한 칸씩 늘리며 같은지 확인
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1

            # 팰린드롬 부분 리턴
            return s[left:right]

        # 예외처리 (길이가 2 이하인 문자열)
        if (len(s) == 1) or (len(s) == 2 and s[0] == s[1]):
            return s
        elif len(s) == 2 and s[0] != s[1]:
            return s[0]

        # 팰린드롬 찾기
        result = ""
        for i in range(len(s)-1):
            result = max(check_palindrome(i, i+1), # 짝수 길이 팰린드롬
                         check_palindrome(i, i+2), # 홀수 길이 팰린드롬
                         result,
                         key=len)

        return result
