"""
https://leetcode.com/problems/permutations/

46. Permutations

난이도: Medium

시작: 21.08.18 10:27
끝: 21.08.18 10:34	
성공: correct

메모리:  KB
시간:   ms

[아이디어]
result = []
dfs(picked, topick):
    for i in topick:
        picked.append(i)
        dfs(picked, topick에서 i 뺀 것)
        picked.pop(i)


[시간복잡도]
O(n!)


[실수]
# topick.remove를 하면 참조로 넘어가기 때문에 다음 루프에서도 i가 삭제된 상태가 된다.
dfs(picked, topick.remove(topick[i])) 

[검색]
https://ooyoung.tistory.com/49
1. del : 인덱스로 삭제
2. remove( ) 함수 : 값으로 삭제
    - 맨 앞의 값만 지워줌


[개선/추가사항]



"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(picked, topick):
            if not topick:
                result.append(picked[:])
            for i in range(len(topick)):
                picked.append(topick[i])
                dfs(picked, topick[:i]+topick[i+1:])
                picked.pop()
        dfs([], nums)
        return result


# 실수
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(picked, topick):
            if not topick:
                result.append(picked[:])
                return
            for i in range(len(topick)):
                # 여기서 오류남
                picked.append(topick[i])
                # dfs(picked, topick[:i]+topick[i+1:])
                # topick.remove를 하면 참조로 넘어가기 때문에 다음 루프에서도 i가 삭제된 상태가 된다.
                dfs(picked, topick.remove(topick[i])) 
                picked.pop()
        dfs([], nums)
        return result