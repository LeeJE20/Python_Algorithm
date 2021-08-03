# 교재 풀이 (python ver)
# p.689
# https://www.algospot.com/judge/problem/read/TRAVERSAL

# def slice(v, a, b):
#     return v[a:b]

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

