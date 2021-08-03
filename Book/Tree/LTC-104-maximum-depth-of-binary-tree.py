# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        pass
        

import collections

# 풀이1: 반복 구조로 BFS 풀이
def maxDepth(self, root:TreeNode)-> int:

    if root is None:
        return 0



    queue = collections.deque([root])
    # 현재 깊이
    depth = 0

    # 현재 깊이 depth에 해당하는 모든 노드가 들어 있음
    # bfs에 while의 반복 횟수: 높이
    while queue:
        depth += 1
        # 부모 노드 개수 만큼만 실행
        for _ in range(len(queue)):
            # 하나씩 꺼냄
            cur_root = queue.popleft()
            
            # 자식노드가 있으면 큐에 삽입한다.
            # if cur_root.has_child():
            #     queue.append(cur_root.child)
            if cur_root.left: 
                queue.append(cur_root.left)
            if cur_root.right:
                queue.append(cur_root.right)

    # BFS 반복 횟수 == 깊이
    return depth
            
    
    return depth