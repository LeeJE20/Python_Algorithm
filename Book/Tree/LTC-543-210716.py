# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    diameter = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def getHeight(root: TreeNode) -> int:
            # 21.07.16 23:22 시작
            # 아이디어
            # dfs - 리프에서부터 높이를 구한다.
            # 리프의 높이는 0이다.
            # 현재 노드의 후보 값은 왼쪽 높이 + 오른쪽 높이이다.

            # 끝: 21.07.16 23:45
            if root is None:
                return -1

    #         stack = collections.deque(root)

    #         while stack:

            left = getHeight(root.left)
            right = getHeight(root.right)
            self.diameter = max(self.diameter, left+right+2)
            return max(left, right) + 1
    
        getHeight(root)
        return self.diameter
            