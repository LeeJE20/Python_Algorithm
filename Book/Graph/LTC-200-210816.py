"""
https://leetcode.com/problems/number-of-islands/

Number of Islands

난이도: medium

시작: 21.08.16 22:19
끝: 21.08.16 22:31
성공: correct

메모리: 15.5 MB, less than 55.54%
시간: 124 ms, faster than 96.63%


[아이디어]
dfs


[시간복잡도]
전부 훑어봐야하므로 O(n^2 + 노드 개수)


[실수]
* 인덱스 처리
    # i-1 >= 0으로 해야하는데 복사하다가 i-1 >= x으로 해버림
    실수 방지: 인덱스 왔다갔다 하는 부분은 실수 방지를 위해 노가다로 하지 말고
        배열에 [[1, 0], [-1, 0], [0, 1], [0, -1]] 이렇게 넣은 다음 
        for로 돌면서 모든 방향에서(미만, 초과) 인덱스 검사를 하자.

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        y = len(grid)
        x = len(grid[0])
        def dfs(j, i):
            grid[j][i] = '0'
            if (j+1 < y) and grid[j+1][i]=='1':
                dfs(j+1, i)

            if (j-1 >= 0) and grid[j-1][i]=='1':
                dfs(j-1, i)

            if (i+1 < x) and grid[j][i+1]=='1':
                dfs(j, i+1)

            # 실수: 복사하다가 i-1 >= x으로 해버림
            if (i-1 >= 0) and grid[j][i-1]=='1':
                dfs(j, i-1)

        count = 0
        for j in range(y):
            for i in range(x):
                if grid[j][i] == '1':
                    dfs(j, i)
                    count += 1

        return count
            