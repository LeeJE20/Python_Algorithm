# n개중 r개를 뽑는 경우의 수

# 재귀
def bino(n: int, r: int)-> int:
    # 기저: n = r (모든 원소를 다 고르는 경우) 
    # 혹은 r = 0 (고를 원소가 없는 경우)
    if (r == 0 or n == r): return 1
    return bino(n-1, r-1) + bino(n-1, r)


# 메모이제이션

# -1로 초기화해둔다.
cache = [[-1]* 30 for _ in range[30]]
def bino2(n: int, r: int) -> int:
    # 기저
    if (r == 0 or n == r): return 1

    # -1이 아니라면 한 번 계산했던 값이니 곧장 반환
    if (cache[n][r] != -1):
        return cache[n][r]
    
    # 직접 계산한 뒤 배열에 저장
    cache[n][r] = bino2(n-1, r-1) + bino2(n-1, r)
    return cache[n][r]


