"""
https://leetcode.com/problems/gas-station/


시작: 21.05.11 12:13
끝: 21.05.11 12:13
성공: 

[아이디어]



[시간복잡도]



[실수]


[검색]


[개선/추가사항]

"""

# 내 코드
class Solution:
    def fib(self, n: int) -> int:
        arr = [0, 1, 1] + ([0] * (n-2))
        for i in range (3, n+1):
            arr[i] = arr[i-1] + arr[i -2]
        return arr[n]


# 교재 메모이제이션
# 교재 타뷸레이션


# 교재 두 변수만 이용해 풀이
# 공간 복잡도가 O(1)이 된다.
def fib(self, N: int) -> int:
    x, y = 0, 1
    for i in range(0, N):
        x, y = y, x + y
    return x