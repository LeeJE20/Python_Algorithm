# 재귀 호출에서 시작하기
def solve1_recursion():
    n: int # board size
    board = [[0]*100 for _ in range(100)]

    def jump(y: int, x: int) -> bool:
        # 기저 사례: 게임판 밖을 벗어난 경우
        if (y >= n) or (x >= n):
            return False

        # 기저: 마지막 칸에 도착한 경우
        if (y == n-1) and (x == n-1):
            return True

        jump_size: int = board[y][x]

        return jump(y + jump_size, x) or jump(y, x+jump_size)


# 메모이제이션 적용하기
def solve2_memoization():
    n: int # board size
    board = [[0]*100 for _ in range(100)]
    cache = [[0]*100 for _ in range(100)]

    def jump2(y: int, x: int) -> int:
        # 기저 사례: 게임판 밖을 벗어난 경우
        if (y >= n) or (x >= n):
            return 0

        # 기저: 마지막 칸에 도착한 경우
        if (y == n-1) and (x == n-1):
            return 1

        # 메모이제이션
        ret = cache[y][x]
        if (ret != -1): return ret
        jump_size: int = board[y][x]
        ret = jump2(y + jump_size, x) or jump2(y, x+jump_size)
        cache[y][x] = ret
        return ret

# 다른 해법
# 그래프(7부)로 모델링해보면 아주 간단한 도달 가능성 문제가 됩니다.