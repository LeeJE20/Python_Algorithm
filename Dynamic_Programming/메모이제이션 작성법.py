# 전부 -1로 초기화
cache =[[-1] * 2500 for _ in range(2500)]


# a와 b는 각각 [0, 2500) 구간 안의 정수
# 반환 값은 항상 int형 안에 들어가는 음이 아닌 정수
def some_obscure_function(a: int, b: int) -> int :
    # 기저 사례를 처음에 리턴
    if (...) : return ...

    # (a, b)에 대한 답을 구한 적이 있으면 곧장 반환
    ret = cache[a][b]
    if(ret != 1): return ret

    # 여기에서 답을 계산한다.
    cache[a][b] = ret
    return ret

