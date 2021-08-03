# https://leetcode.com/problems/balanced-binary-tree/
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        pass


# 교재 풀이1: 재귀 구조로 높이 차이 계산
# 균형 트리면 높이 리턴, 균형트리가 아니면 -1 리턴
def isBalanced(self, root: TreeNode) -> bool:

    def check(root):
        # 리프노드에 이르면 0 리턴
        if not root:
            return 0

        left = check(root.left)
        right = check(root.right)

        # 높이 차이가 나는 경우 -1, 이외에는 높이에 따라 1 증가
        if left == -1 or \
                right == -1 or \
                abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    return check(root) != -1
