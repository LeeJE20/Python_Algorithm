# https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    longest: int = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 풀이1: 상태값 누적 트리 DFS
        def dfs(node: TreeNode) -> int:
            if not node:
                # 상태값
                return -1
            
            # 재귀 호출을 통해 왼쪽, 오른쪽의 각 리프 노드까지 DFS로 탐색
            # 자식 노드가 하나도 없으면 -1이 리턴된다.
            left = dfs(node.left)
            right = dfs(node.right)

            # 최종 결과가 될 가장 긴 경로 (거리)
            self.longset = max(self.longest, left + right + 2)
            # 상태값
            return max(left, right) + 1
        
        dfs(root)
        return self.longest

    # 중첩 함수를 사용할 때 클래스 변수 self.longest를 사용한 이유
    # 중첩 함수에서 부모 함수의 변수를 재할당하게 되면 참조 ID가 변경되며 별도의 로컬 변수로 선언된다.
    # longest가 숫자, 문자같은 불변 객체가 아니라 리스트, 딕셔너리 같은 자료형이라면 
    #   append() 등을 이용해 재할당 없이 조작 가능


    