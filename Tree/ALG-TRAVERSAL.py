"""
https://www.algospot.com/judge/problem/read/TRAVERSAL

TRAVERSAL

난이도: 하

시작: 21.07.21 23:30
끝: 21.07.29 10:46
성공: wrong

메모리:  KB
시간:  44 ms

[아이디어]
pre_order: 루트들이다.
pre_order에서 찾은 루트 기준으로 in_order를 2개를 나누면, 왼쪽 서브트리와 오른쪽 서브트리이다.

1)pre_order에서 루트를 찾는다.
2) in_order를 left와 right로 나눈다.
3) 
    left의 개수가 0이면
        right에 대해 1, 2반복
            right의 개수가 0이면: 
                print root
                return
    left의 개수가 0이 아니면:
        left에 대해 1, 2 반복


[시간복잡도]
N개의 노드에 대해..
preorder을 훑고(N), 그것을 루트로 삼아 inorder에서 2개로 나눈뒤 2개에 대해 각각 이 계산을 실행한다.
N개의 노드를 가진 이진 트리의 높이만큼의 계산 횟수라고 칠 수 있다.
따라서 O(log2(n))



[실수]
    # 실수: 아래처럼 하면 배열의 크기가 1이다...
    # if (left_idx+1 ==right_idx):
    # 실수 방지: 배열의 크기가 0이려면 l_inx와 r_idx가 같아야 한다.
    # 원소의 개수가 하나 있는 배열의 인덱스를 생각해보자.
    # ["원소하나"]의 시작 인덱스는 0, (끝 인덱스+1)는 1이므로 배열의 크기는 ((끝+1)-시작)인 1이다.


[검색]



[개선/추가사항]



[고수풀이]
링크: 교재

메모리:  KB
시간:   ms


접근법: 나와 같다


배울 점: 
preorder를 잘라서 그대로 넘기면서 기저 처리를 더 간단하게 했다.
index가 아니라 개수로 처리해서 더 간단해졌다.
python은 어차피 call by reference 비슷하니까, 배열을 넘기는게 계산이 편리하면 배열을 넘기자.

코드

# 트리의 전위탐색 결과와 중위탐색 결과가 주어질 때 후위탐색 결과를 출력한다.
def print_post_order(preorder, inorder):
    # 트리에 포함된 노드의 수
    N = len(preorder)

    # 기저: 텅 빈 트리면 곧장 종료
    if not preorder: return

    # 이 트리의 루트는 전위 탐색 결과로부터 곧장 알 수 있다.
    root = preorder[0]

    # 이 트리의 왼쪽 서브트리의 크기는 중위 탐색 결과에서 루트의 위치를 찾아서 알 수 있다.
    L = inorder.find(root)

    #  오른쪽 서브트리의 크기는 N에서 왼쪽 서브트리와 루트를 빼면 알 수 있다.
    R = N - 1 - L

    # 왼쪽과 오른쪽 서브트리의 순회 결과를 출력
    print_post_order(preorder[1, L+1], inorder[0, L])
    print_post_order(preorder[L+1, N], inorder[L+1, N])

    # 후위 순회이므로 루트를 가장 마지막에 출력
    print(root, end = " ")


"""

import sys
input = sys.stdin.readline
# print = sys.stdout.write

idx = 0
N = 0

"""
@param ilidx: 현재 대상으로 하는 in_order 부분의 시작 인덱스
@param iridx: 현재 대상으로 하는 in_order 부분의 끝 인덱스

"""
def find_postorder(pre_order, in_order, ilidx, iridx):
    global idx
    global N
    # print("-----------------------------")
    # print(f"in_order: {in_order[ilidx: iridx]}")

    # 배열의 크기가 0이면 리턴
    # 실수: 아래처럼 하면 배열의 크기가 1이다...
    # if (ilidx+1 ==iridx):
    if (ilidx ==iridx):
        # print("배열의 크기가 0이므로 리턴")
        return

    if (idx < N):
        # 1)pre_order에서 루트를 찾는다.
        root = pre_order[idx]
        idx += 1
    else:
        return

    # if idx == 7:
    #     return

    
    # 2) in_order를 left와 right로 나눈다.
    root_idx_inorder = in_order.index(root)
    # 인덱스
    left = [ilidx, root_idx_inorder]
    right = [root_idx_inorder+1, iridx]

    # if (left[0]+1 == left[1]) and (right[0]+1 == right[1]):
    #     print(root, end = " ")
    #     return
    
    
    # 3) 
    # left의 개수가 0이면

    # if left[0]+1 == left[1]:
    #     right에 대해 1, 2반복
        
    #         right의 개수가 0이면: 
    #             print root
    #             return
    # left의 개수가 0이 아니면:
    #     left에 대해 1, 2 반복

    # print(f"root: {root}")
    # print("find left")
    find_postorder(pre_order, in_order, left[0], left[1])
    # print(f"root: {root}")
    # print("find right")
    find_postorder(pre_order, in_order, right[0], right[1])
    print(root, end = " ")
    return

def solve():
    global N
    global idx

    N = int(input())
    idx = 0
    pre_order = list(map(int, input().split()))
    in_order = list(map(int, input().split()))
    find_postorder(pre_order, in_order, 0, N)
    print()




C = int(input())

for i in range(C):
    solve()

