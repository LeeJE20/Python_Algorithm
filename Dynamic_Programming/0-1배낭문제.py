#  짐을 쪼갤 수 없는 배낭 문제

# 용량 15kg 가방의 가치를 가장 높게 하는 방법?

# 가치, 무게
carge = [
    (4, 12), 
    (2, 1), 
    (10, 4), 
    (1, 1), 
    (2, 2), 
]

r = zero_one_knapsack(cargo)



def zero_one_knapsack(cargo):
    capacity = 15
    # 타뷸레이션
    # 6 *16 행렬 형태의 중간 결과 테이블
    # 6: 모든 짐의 개수 + 1 ,  16: 배낭의 최대 용량 + 1
    pack = [] 

    for i in range(len(cargo) + 1):
        pack.append([])
        for c in range(capacity + 1):
            if i == 0 or c == 0: 
                pack[i].append(0)
            elif cargo[i-1][1] <= c:
                pack[i].append(
                    max(
                        cargo[i-1][0] + pack[i-1][c - cargo[i-1][1]],
                        pack[i-1][c]
                    )
                )
            else:
                pack[i].append(pack[i-1][c])

    return pack[-1][-1]