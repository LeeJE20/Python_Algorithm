# https://leetcode.com/problems/combinations/

# 21.08.16

"""아이디어
순서 상관 없이 뽑기

dfs(picked, topick, k)
    if k == 0
        picked 저장
        return
    
    for i in range(len(topick)):
        next = topick에서 i와 i 앞부분 제외
        picked.append(i)

        dfs(picked, next, k-1)

        picked에서 i 제거

"""


# 풀이1: DFS로 k개 조합 생성
def combine(self, n: int, k: int) -> List[List[int]]:
    results = []

    def dfs(elements, start: int, k: int):
        if k == 0:
            results.append(elements[:])
            return
    
        # 자신 이전의 모든 값을 고정하여 재귀 호출
        # 자신 이후의 값만 넘길 수 있게 한다.
        for i in range(start, n+1):
            elements.append(i)
            dfs(elements, i+1, k-1)
            elements.pop()

    
    dfs([], 1, k)
    return results



# 풀이2: itertools 모듈 사용
import itertools
def combine(self, n: int, k: int) -> List[List[int]]:
    return list(itertools.combinations(range(1, n+1), k))