"""
https://leetcode.com/problems/valid-palindrome/

125. Valid Palindrome

난이도: Easy

시작: 21.09.15 10:35
끝: 21.09.15 10:43
성공: 2회 성공

메모리:  15.3 MB, less than 31.66%
시간:   51 ms, faster than 48.89%

[아이디어]
전부 대문자로 바꿔둔다.
숫자, 문자만 리스트에 넣어둠
투포인터로 체크



[시간복잡도]
O(n)


[실수]



[검색]
s.upper() 함수는 원본에는 변화가 없다.
s = s.upper() 이렇게 대입해줘야 한다.


[개선/추가사항]


"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 문법
        # s.upper을 한 다음 s에 다시 할당해야함.
        # s.upper()
        s = s.upper()

        ss = []
        for i in s:
            if i.isalnum():
                ss.append(i)

        l, r = 0, len(ss)-1

        while l<r:
            if ss[l] != ss[r]:
                return False
            l += 1
            r -= 1

        return True