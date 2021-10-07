# https://leetcode.com/problems/number-of-islands/

# 내 풀이
# 배열 훑으면서 dfs
# 실수: grid가 str인데 int인줄 알았다.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x = int(len(grid[0]))
        y = int(len(grid))
        
        count = 0
        
        print(f"{x}, {y}")
        for i in range(x):
            for j in range(y):
                current = int(grid[j][i])
                if current == 1:
                    stack = [[j, i]]
                
                    while stack:
                        m, n = stack.pop()
                        # print(f"now: {m}, {n}")
                        # for a in grid:
                        #     print(" ".join(a))
                        # grid[m][n] = 0
                        
                        # 우, 상, 좌, 하
                        move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
                    
                        for yy, xx in move:
                            # 연결된 부분 중 방문 안 한 부분이 있다
                            if ((m+yy < y) and (n + xx < x) and 
                                    (0 <= m+yy) and (0 <= n + xx) and
                                    grid[m+yy][n + xx] == "1" ):
                                # print(f"move: {m+yy}, {n + xx}")
                                grid[m+yy][n + xx] = "0"
                                stack.append([m+yy, n + xx])
        
                    count += 1
            
        return count


# 풀이1: DFS로 그래프 탐색
# 동서남북이 모두 연결된 그래프로 가정
# 네 방향 각가 DFS 재귀를 이용해 탐색을 끝마치면 1 증가
def numIslands(self, grid: List[List[str]]) -> int:
    def dfs(i, j):
        # 더 이상 땅이 아닌 경우 종료
        if i < 0 or i >= len(grid) or \
            j < 0 or j >= len(grid[0]) or \
            grid[i][j] != '1':
            return

        grid[i][j] = '0'

        #동서남북 탐색
        dfs(grid, i+1, j)
        dfs(grid, i-1, j)
        dfs(grid, i, j+1)
        dfs(grid, i, j-1)
    


    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                dfs(i, j)
                # 모든 육지 탐색 후 카운트 1 증가
                count += 1
    
    return count


