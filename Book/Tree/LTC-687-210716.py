# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 시작: 21.07.16 23:46
# 끝: 21.07.16 23:59
class Solution:
    longest = 0
    def longestUnivaluePath(self, root: TreeNode) -> int:
        # 현재노드가 포함되는 longestUnivaluePath 리턴
        def longestThisNode(root: TreeNode)-> int:
            if root is None:
                return -1
            
            left = longestThisNode(root.left)
            right = longestThisNode(root.right)
            if root.left and root.right and root.val == root.left.val and root.val == root.right.val:
                
                self.longest = max(self.longest, left + right + 2)
                return max(left, right) + 1
            
            elif root.left and root.val == root.left.val:
                self.longest = max(self.longest, left + 1)
                return left + 1
            elif root.right and root.val == root.right.val:
                self.longest = max(self.longest, right + 1)
                return right + 1
            else:
                return 0
            
        longestThisNode(root)
        return self.longest