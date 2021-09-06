"""
https://leetcode.com/problems/combinations/

77. Combinations

난이도: Medium

시작: 21.08.18 10:54
끝: 21.08.18 11:04	
성공: correct

메모리: 15.7 MB, less than 78.90%
시간:   524 ms, faster than 40.92%

[아이디어]
result = []
dfs(picked, topick, k):
    if k==0:
        result.append(picked[:])
        return
    for i in range(topick):
        picked.append(topick[i])
        dfs(picked, picked[i+1, :], k-1)
        picked.pop()




[시간복잡도]
O(nCk))


[실수]
# 실수: 슬라이싱 할때 ,는 쓰면 안 된다.
topick[i+1, :] => topick[i+1:]

[검색]



[개선/추가사항]



"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def dfs(picked, topick, k):
            if k==0:
                result.append(picked[:])
                return
            for i in range(len(topick)):
                picked.append(topick[i])
                # 실수: 슬라이싱 할때 ,는 쓰면 안 된다.
                # dfs(picked, topick[i+1, :], k-1)
                dfs(picked, topick[i+1:], k-1)
                picked.pop()

        dfs([], [i for i in range(1, n+1)], k)
        return result