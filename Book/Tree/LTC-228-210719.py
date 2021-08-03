# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
#         ~~ 재귀
#       24ms, 14.3MB
        # if root is None:
        #     return root
        # left = self.invertTree(root.left)
        # right = self.invertTree(root.right)
        # root.left = right
        # root.right = left
        # return root
    
    ## bfs
    #       32ms, 14.3MB
        if root is None:
            return root
        
        q = collections.deque([root])
        
        while q:
            now = q.popleft()
#             left = now.left
#             right = now.right
            
#             now.left = right
#             now.right = left
            now.left, now.right = now.right, now.left
            # print(f"now.left: {now.left}")
            # print(f"now.right: {now.right}")
            if now.left:
                q.append(now.left)
                
            if now.right:
                q.append(now.right)
                
        return root
                
        
    
    
    