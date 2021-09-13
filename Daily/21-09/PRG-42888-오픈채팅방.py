"""
https://programmers.co.kr/learn/courses/30/lessons/42888

오픈채팅방

난이도: 레벨 2

시작: 21.09.13 11:11
끝: 21.09.13 11:23
성공: 1회 correct


[아이디어]
딕셔너리 {유저아이디: 닉네임}
record를 2번 돈다.

1번째
enter, change만 확인: 각 유저아이디에 닉네임 적기


2번째
enter, leave만 확인: result 문구 작성

[시간복잡도]
배열 훑어보기
O(n)

[실수]



[검색]



[개선/추가사항]
굳이 defaultdict를 안 써도 된다.



[고수풀이]
링크: 

접근법:
나와 같음

배울 점: 


코드


"""

import collections
def solution(record):
    
    record = list(map(lambda x: x.split(), record))
    
    d = collections.defaultdict(str)

    # 딕셔너리에 유저아이디: 닉네임 적기
    for i in range(len(record)):
        if record[i][0] == "Leave":
            continue
        else:
            d[record[i][1]] = record[i][2]

    # 문구 작성
    answer = []
    for i in range(len(record)):
        if record[i][0] == "Enter":
            answer.append(str(d[record[i][1]])+"님이 들어왔습니다.")
        elif record[i][0] == "Leave":
            answer.append(str(d[record[i][1]])+"님이 나갔습니다.")
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))