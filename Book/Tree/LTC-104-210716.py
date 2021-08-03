"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/submissions/

maximum-depth-of-binary-tree

난이도: 

시작: 21.07.16 
끝: 21.07.16 
성공: correct

메모리: 16200 KB
시간:  32 ms

[아이디어]
1.
재귀로 푼다. 
현재 노드까지의 max = 지금까지의 max +1

3. BFS



"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        ## ~~ 1. recursion
        if root is None:
            return 0
        depth = 0
        
        depth = max(depth, self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
        return depth
            

    
        # ## ~~ 2. BFS
        # if root is None:
        #     return 0
        
        # dq = collections.deque()
        
        # dq.append(root)
        # depth = 0
        
        # while dq:
        #     depth += 1
            
        #     for _ in range(len(dq)):
        #         node = dq.popleft()
            
        #         if node.left:
        #             dq.append(node.left)
        #         if node.right:
        #             dq.append(node.right)
        
        # return depth
            
        