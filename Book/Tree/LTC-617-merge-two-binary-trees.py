# 내 풀이
# https://leetcode.com/problems/merge-two-binary-trees/
# 21.05.31
# # Q45. 이진 트리 반전 문제 재귀 풀이처럼 풀었다.
# 재귀로 하니까 너무 쉽게 풀렸다. 참 좋은 재귀!

class Solution:
    # 합쳐진 트리를 리턴해주는 함수
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 and root2:
            # left끼리의 합쳐진 트리
            left = self.mergeTrees(root1.left, root2.left)
            # right끼리의 합쳐진 트리
            right = self.mergeTrees(root1.right, root2.right)
            # 가운데 합치기
            node = TreeNode(root1.val + root2.val)
            # 연결
            node.left = left
            node.right = right
            
            return node
        elif root1: return root1
        elif root2: return root2
        else: return None



# 교재 풀이1: 재귀 탐색
def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    # 각각 이진 트리의 루트부터 시작해 합쳐 나가면서 좌, 우 자식 노드 또한 병합될 수 있도록 한다.
    # 리턴 순서만 놓고 본다면 탐색 순서는 후위 순회이다.
    if t1 and t2:
        node = TreeNode(t1.val + t2.val)
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)

        return node
    # 어느 한 쪽에 노드가 없다면 존재하는 노드만 리턴
    # 양쪽 노드가 모두 존재하지 않는다면 None이 리턴된다.
    else: return t1 or t2
    