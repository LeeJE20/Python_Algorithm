"""
https://programmers.co.kr/learn/courses/30/lessons/72412

순위 검색

난이도: 레벨 2

시작: 21.05.11 11:04
끝: 21.05.11 12:13
성공: 

메모리:  KB
시간:   ms

[아이디어]



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





"""
사람들의 숫자를 순서대로 배열에 담아 return

개발언어는 cpp, java, python
직군은 backend, frontend
경력은 junior, senior
소울푸드는 chicken, pizza

각 단어는 공백문자(스페이스 바) 하나로 구분





[조건]은 "개발언어 and 직군 and 경력 and 소울푸드" 
'-' 표시는 해당 조건을 고려하지 않겠다는 의미입니다.
X는 코딩테스트 점수를 의미하며 조건을 만족하는 사람 중 X점 이상 받은 사람은 모두 몇 명인 지를 의미합니다.

"""

"""
아이디어
인원수: n, 문제수: N

그때그떄 하나씩 서치하면 -> nN

정보를 저장해둬야함..

처음에 정렬을 해두고, binary search로 탐색?

1. info를 split으로 분리
2. 전체 정렬
3. binary search로 탐색하기




"""

# def b_search()

# def solution(info, query):

#     info.sort()
#     data = []
#     for i in info:
#         data.append(i.split())


    

#     d = {"cpp":0, "java": 1, "python":2,
#      "backend":0, 'frontend': 1,
#  'junior':0, 'senior': 1,
#  'chicken':0, 'pizza': 1}

#     for i in query:
#         start = 0
#         end = len(data)
#         q = query.split()
#         for j in range(5):
#             if q[j] == "-":
#                 pass
#             else:
#                 while True:
#                     mid = (start+ end)// 2

#                     # 큰 곳을 탐색해야 함
#                     if d[data[mid][j]] < d[q[j]]:
#                         start = mid
#                     # 올바른 값:
#                     elif d[data[mid][j]]==d[q[j]]:
#                         # start와 end 범위 조정
#                         while d[data[start][j]]!=d[q[j]]:
#                             start += 1
#                         while d[data[end][j]]!=d[q[j]]:
#                             end -= 1
#                         break
#                     # 작은 곳을 탐색해야 함
#                     else: 
#                         end = mid
            

#     answer = []
#     return answer

import copy

class Node():
    def __init__(self, n) -> None:
        super().__init__()
        self.start = 0
        self.end = 0
        self.next = n



def solution(info, query):
    d = {"cpp":0, "java": 1, "python":2,
     "backend":0, 'frontend': 1,
 'junior':0, 'senior': 1,
 'chicken':0, 'pizza': 1}

    # info.sort(key= lambda x: (x[4], x[0], x[1], x[2], x[3]))
    info.sort()
    data = [[[[[]for _ in range(2)] for _ in range(2)]for _ in range(2)]for _ in range(3)]
    for i in info:
        dt = i.split()
        data[d[dt[0]]][d[dt[1]]][d[dt[2]]][d[dt[3]]].append(dt[4])

    for i in query:
        q = query.split()

        qu = [q[0], q[2], q[4], q[6]]

        for j in qu:
            if j == "-":
                for 

# solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], "")