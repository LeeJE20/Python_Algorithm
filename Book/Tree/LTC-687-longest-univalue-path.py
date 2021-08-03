# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# https://leetcode.com/problems/longest-univalue-path

# 내 풀이
# 리프부터 올라가면서, 부모랑 달라지면 처음부터 다시 쌓는다.
class Solution:
    longest = 0
    odd_val = 10000
    def longestUnivaluePath(self, root: TreeNode) -> int:
        # 실수: 문제 조건에서 root가 비어있을 수 있음을 간과
        if not root:
            return 0
        
        def dfs(node: TreeNode, parent_val):
            if not node:
                return -1, self.odd_val
            
            a= b = -1
            
            a, a_val = dfs(node.left, node.val)
            b, b_val = dfs(node.right, node.val)
    
            # 자식들이 모두 값이 달라졌으면 현재노드의 상태값은 0이다 (처음부터 쌓기)
            ret = 0
            # 양쪽 자식 모두 부모(현재노드)와 값이 같다면
            if (a_val == node.val and b_val == node.val):
                self.longest = max(self.longest, a+b+2)
                # 현재노드의 상태값 저장
                ret = max(a, b) + 1
            # 한쪽 자식만 현재노드와 값이 같다면
            elif (a_val == node.val):
                ret = a + 1
            elif (b_val == node.val):
                ret = b + 1

            # 한쪽 자식 방향으로만 같은 값이 있는 경우
            self.longest = max(self.longest, ret)
            
            return ret, node.val
        
        dfs(root, root.val)
        return self.longest        



# 교재풀이 1: 상태값 거리 계산 DFS
class Solution:
    result: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if node is None:
                return 0

            # 존재하지 않는 노드까지 DFS 재귀 탐색
            # 리프 노드에 이르러서 값을 리턴받게 된다.
            left = dfs(node.left)
            right = dfs(node.right)

            # 자식 노드가 동일한 값인지 확인
            # 부모 노드와 동일하면 거리를 1 증가한다.
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 합이 가장 큰 값을 최종 결과로 한다
            # 왼쪽과 오른쪽 자식 노드 간 거리의 합의 최댓값이 결과
            result = max(result, left + right)

            # 다음번 백트래킹 시 계산을 위해 상태값을 세팅해 부모 노드로 올린다.
            # 현재 노드는 양쪽 자식 노드를 모두 연결할 수 있지만, 
            # 현재 노드의 부모 노드에서는 지금의 양쪽 자식 노드를 연결할 수 없다
            # 단방향이므로, 양쪽 자식 노드 중 어느 한쪽 자식만 택할 수 있다
            # 자식노드 상태값 중 큰 값 리턴
            return max(left, right)


        dfs(root)
        return self.result