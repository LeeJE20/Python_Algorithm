# 내 풀이
# 시작: 2021.05.31 13:50
# 끝: 2021.05.31 23:08
# 결과: correct


# 루트-오른쪽-왼쪽 순서로 읽는다.
# bfs로 읽어나가며 좌우 반전
import collections


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        q = deque()
        if (root):
            q.append(root)

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                tmp = node.left
                node.left = node.right
                node.right = tmp

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root


# 교재 풀이1: 파이썬다운 방식
# 재귀로 풀이
# 리프노드까지 내려가서 백트래킹하면서 스왑 (Bottom-Up)
def invertTree(self, root: TreeNode) -> TreeNode:
    if root:
        root.left, root.right =\
            self.invertTree(root.right), self.invertTree(root.left)
        return root
    return None


# 풀이2: 반복 구조로 BFS
# 42번 이진 트리의 최대 깊이 문제와 비슷
# 부모 노드부터 스왑하면서 계속 아래로 내려가는 하향 (Top-Down)


def invertTree(self, root: TreeNode) -> TreeNode:
    queue = collections.deque([root])

    # 내부에 for문이 없다. 자유롭게 스왑하면서 queue에 추가
    # 먼저 삽입된 노드는 반복 구조로 계속 스왑되면서 자식노드가 계속해서 큐에 추가된다.
    while queue:
        node = queue.popleft()

        # 부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left

            queue.append(node.left)
            queue.append(node.right)

    return root


# 풀이 3: 반복 구조로 DFS
# BFS와 스택 pop을 했다는 점만 다르다.
def invertTree(self, root: TreeNode) -> TreeNode:
    stack = collections.deque([root])

    while stack:
        stack = stack.pop()

        # 부모 노드부터 하향식 스왑
        if node:
            node.left, node.right = node.right, node.left

            stack.append(node.left)
            stack.append(node.right)

    return root

# 풀이 4: 반복 구조로 DFS 후위 순회
# 앞서 풀이는 전위 순회 형태로 했지만, 후위 순회로 변경해도 된다.


def invertTree(self, root: TreeNode) -> TreeNode:
    stack = collections.deque([root])

    while stack:
        stack = stack.pop()

        # 부모 노드부터 하향식 스왑
        if node:
            stack.append(node.left)
            stack.append(node.right)

            # 후위 순회
            node.left, node.right = node.right, node.left
    return root
