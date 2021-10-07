# https://leetcode.com/problems/combination-sum/

# 21.08.16

"""아이디어
candidates하나씩 더해가면서 target 넘으면 끝!
dfs로 한다.

dfs(picked, sum)
    for i in candidates:
        if sum+i < target:
            picked.append(i)
            dfs(picked, sum+i)
            picked.pop(i)
        elif sum+1 == target:
            picked 저장
            return
"""

# 풀이1: DFS로 중복 조합 그래프 탐색
# 조합-> 각각의 노드가 자기 자신부터 하위 원소까지의 나열
# -> 부모의 값부터 시작하는 그래프로 구성

def combinationSum(self, candidates: List[int], target:int) -> List[List[int]]:
    result = []

    def dfs(csum, index, path):
        # 종료 조건
        if csum<0:
            return
        if csum == 0:
            result.append(path)
            return

        # 자신부터 하위 원소까지의 나열 재귀 호출
        for i in range(index, len(candidates)):
            dfs(csum -candidates[i], i, path + [candidates[i]])

    
    dfs(target, 0, [])
    return result