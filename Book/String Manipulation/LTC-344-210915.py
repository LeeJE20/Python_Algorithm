"""
https://leetcode.com/problems/reverse-string/

344. Reverse String

난이도: Easy

시작: 21.09.15 11:04
끝: 21.09.15 11:11
성공: 

메모리:  18.4 MB, less than 81.48%
시간:   192 ms, faster than 90.31%

[아이디어]



[시간복잡도]



[실수]



[검색]



[개선/추가사항]
"""


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s)-1
        while l<r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
