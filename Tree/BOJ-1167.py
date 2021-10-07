"""
https://www.acmicpc.net/problem/1167

트리의 지름

난이도: 골드 3

시작: 21.06.08 00:29
끝: 21.06.08 1:30
성공: 

메모리:  KB
시간:   ms

[아이디어]
리프에서부터 백트래킹

result: 정답
solve(n): 트리의 높이(가중치) 최댓값 리턴

음.. 해보니까 꼭 루트(여기서는 1)이 포함되지 않을 때가 정답일 수도 있다.
이를 위해서는 모든 노드에 대해 dfs를 수행해봐야 하는데 중복이 많아서 비효율적이다...


[시간복잡도]



[실수]



[검색]



[개선/추가사항]



[고수풀이]
링크: 

메모리:  KB
시간:   ms


접근법:


배울 점: 


코드



"""

import sys
from collections import defaultdict
input = sys.stdin.readline
# print = sys.stdout.write

N = int(input())
d = defaultdict(dict)
for _ in range(N):
    arr = list(map(int, input().split()))
    # len(arr)-2 : 마지막의 -1은 i에 안 들어오게 한다.
    for i in range(1, len(arr)-2, 2):
        # 딕셔너리에 연결. 
        # d[현재노드]
        # {key: arr[i] 연결된 노드, value: arr[i+1] 가치} 를 저장
        d[arr[0]][arr[i]] = arr[i+1]

print(d)

result = -1
# 리턴값: node의 상태값 (리프에서 node까지의 가치 합 중 최댓값)
def solve(node: int) -> int:
    global result

    
    # node의 자식들을 찾는다.
    # 실수: keys가 아니라 keys()이다.
    # https://wikidocs.net/16
    # 리스트로 변환하려면 []만 씌워서는 안 된다. list()로 감싸야 한다.
    children = list(d[node].keys())

    print(f"\nnode: {node}")
    print(f"children: {children}")
    # 리프노드라면:
    if not children:
        print(f"{node}의 상태값: 0")
        return 0

    # 리프에서 node까지의 가치 합들을 찾는다.

    # values가 최소 2개의 원소를 가질 수 있게 0을 넣어둔다.
    # max_value를 구할 때 사용..
    values = [0]
    for child in children:
        # 자식에서 부모로의 연결을 삭제한다.
        # 검색: 딕셔너리 삭제
        # print(f"d[child]: {d[child]}")
        del d[child][node]
        # print(f"삭제 후 d[child]: {d[child]}")

        values.append(solve(child) + d[node][child])

    values = sorted(values)
    state = values[-1]+ values[-2]
    result = max(result, state)

    print(f"{node}의 상태값: {state}")
    return state

# 1번 노드를 루트라고 생각하고 만들자.

solve(1)
print(result)
    
    





# print("\n".join(map(str,arr)) + "\n")