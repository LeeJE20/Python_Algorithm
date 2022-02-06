"""
https://programmers.co.kr/learn/courses/30/lessons/42889

실패율

난이도: level 1

시작: 21.10.15 10:23
끝: 21.10.15 10:58
성공: 	
    1. 실패 (런타임 에러)
    2. 통과 : 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.

메모리:  KB
시간:   ms

[아이디어]
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수: rnc(reached not clear)
스테이지에 도달한 플레이어 수: r(reached)

rnc: stages 를 Counter 모듈로 카운트


스테이지가 3개 있다면
r[4] = rnc[4]
r[3] = r[4] + rnc[3]
r[2] = r[3] + rnc[2]
r[1] = r[2] + rnc[1]

failure[1] = [rnc[1] / r[1], 1]
failure.sort






[시간복잡도]



[실수]



[검색]



[개선/추가사항]



[고수풀이]
링크: 

메모리:  KB
시간:   ms


접근법:


배울 점: 


코드



"""
from collections import Counter
def solution(N, stages):
    # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수: rnc(reached not clear)
    # 스테이지에 도달한 플레이어 수: r(reached)

    # rnc: stages 를 Counter 모듈로 카운트
    rnc = Counter(stages)
    # print(rnc)
    # 스테이지가 3개 있다면
    # r[4] = rnc[4]
    # r[3] = r[4] + rnc[3]
    # r[2] = r[3] + rnc[2]
    # r[1] = r[2] + rnc[1]

    r = {}
    r[N+1] = rnc[N+1]

    failure = [[None, i] for i in range(1, N+1)]
    # print(failure)
    for i in range(N, 0, -1):
        r[i] = r[i+1] + rnc[i]
        # 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
        try:
            failure[i-1][0] = rnc[i]/r[i]
        except:
            failure[i-1][0] = 0
    # print(r)
    # print(failure)
    # failure[1] = [rnc[1] / r[1], 1]
    # failure.sort
    failure = sorted(failure, key = lambda s: (-s[0], s[1]))
    # print(failure)


    # answer = []
    answer = [i[1] for i in failure]
    # print(answer)
    return answer

solution(5, 	[2, 1, 2, 6, 2, 4, 3, 3])