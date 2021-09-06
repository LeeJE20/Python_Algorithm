# https://leetcode.com/problems/permutations/

# 21.08.16

"""
내 풀이 아이디어

picked: 이미 뽑은 것 배열
topick: 아직 안 뽑은 것 배열
dfs(picked, topick)
    if topick이 비었다면:
        return picked

    for i in 주어진 배열
        picked.append(i)
        dfs(picked, topick에 i 뺀 것)


"""

# 풀이1: DFS를 활용한 순열 생성
def permute(self, nums:List[int]) -> List[List[int]]:
    results = []
    # 지금까지 뽑은 숫자
    prev_elements = []

    def dfs(elements):
        # 리프 노드일 때 결과 추가
        if len(elements) == 0:
            # 값만 복사 (참조 관계 없음)
            results.append(prev_elements[:])

        # 순열 생성 재귀 호출
        for e in elements:
            # 현재 숫자를 뺀 나머지
            next_elements = elements[:]
            next_elements.remove(e)

            
            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    dfs(nums)
    return results


# 풀이2: itertools 모듈 사용
import itertools
def permute(self, nums:List[int]) -> List[List[int]]:
    # 튜플
    # return list(itertools.permutaions(nums))

    # 리스트
    return list(map(list, itertools.permutaions(nums)))