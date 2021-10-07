"""
https://programmers.co.kr/learn/courses/30/lessons/77484

로또의 최고 순위와 최저 순위

난이도: 레벨 1

시작: 21.09.13 10:17
끝: 21.09.13 10:36
성공: 2회 correct


[아이디어]
둘 다 정렬시키고 인덱스 훑어가며 같은것 또는 0이 있는지 체크


[시간복잡도]
길이가 6개인 배열로 정해져 있음
따라서 O(1)

길이가 n개라면 정렬때문에 O(nlogn)

[실수]
랭크를 계산할 때 high를 low-(0의 개수)로 했더니 순위가 0위가 나오기도 했다.
일치하는 것이 없어 6등인데, 모두 0이었던 경우  6-6이 되어 0순위가 나온다.

6위는 1개 번호가 일치, 0개 번호가 일치인 경우 모두 6위로 처리해야해서 생긴 문제이다.
따라서 계산할 떄 low와 high를 따로 계산하였다.


[검색]



[개선/추가사항]



[고수풀이]
링크: https://programmers.co.kr/learn/courses/30/lessons/77484/solution_groups?language=python3

접근법:
set의 교집합으로 풀이하였다.
0의 개수를 셀 때에도 count(0) 함수를 사용하였다.

배울 점: 
리스트.count(원소)를 이용하면 해당 원소의 개수를 알 수 있다.
두 리스트에서 같은 값이 있는지 확인하고 싶다면 교집합을 고려해본다.

코드

def solution(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]


"""


# 1차
def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()

    l= 0
    w=0
    same_count = 0
    zero_count = 0


    while l<6 and w < 6:
        if lottos[l] == 0:
            zero_count += 1
            l+=1
        elif lottos[l]==win_nums[w]:
            same_count+=1
            l+=1
            w+=1
        elif lottos[l]>win_nums[w]:
            w+=1
        elif lottos[l]<win_nums[w]:
            l+=1
    
    rank = 6 if same_count<2 else (7-same_count)
    
    answer = [rank - zero_count, rank]
    return answer


# 2차
# 랭크 계산 개선
def solution(lottos, win_nums):
    lottos.sort()
    win_nums.sort()

    # 인덱스
    l= 0
    w=0

    # 일치하는 숫자 개수
    same_count = 0
    # lottos에서 0의 개수
    zero_count = 0


    while l<6 and w < 6:
        if lottos[l] == 0:
            zero_count += 1
            l+=1
        elif lottos[l]==win_nums[w]:
            same_count+=1
            l+=1
            w+=1
        elif lottos[l]>win_nums[w]:
            w+=1
        elif lottos[l]<win_nums[w]:
            l+=1
    
    # 랭크 계산
    low_rank = 6 if same_count<2 else (7-same_count)
    high_rank = 6 if (same_count+zero_count)<2 else (7-(same_count+zero_count))
    
    answer = [high_rank, low_rank]
    return answer
