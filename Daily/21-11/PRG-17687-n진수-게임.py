"""
https://programmers.co.kr/learn/courses/30/lessons/17687

2018 KAKAO BLIND RECRUITMENT
[3차] n진수 게임

level 2

21.11.12
30분 내 풀이

[문제 유형]
구현

[몰랐던 문법]
1. yield 쓰는 법
    - 굳이 안 써도 풀 수는 있다.
2. 문자열을 아스키 코드로 바꾸는 함수
    ord("A")
    chr(45)

[접근 방향]
- n진법으로 변환한 수들을 문자열로 만들고, 
튜브가 말할 숫자는 인덱스를 이용해 찾늗다.
- 숫자를 문자열로 만들떄 dict 활용

[실수]
구해야 하는 n진수로 변환한 문자열 길이를 처음에 t라고 생각함.
튜브가 말해야 하는 개수가 t인 것임.
인원이 m명이므로 m번에 한 번 튜브가 정답을 말함.
따라서 m * t만큼 구해야 나중에 인덱스로 튜브가 t개를 말할 수 있음.

[문제에서 배울 점]
진법 변환 테크닉

[다른 사람 코드]
튜브 순서 구하기를 슬라이싱으로 구할 수 있다.


"""


d = {
    10 : "A",
    11 : "B",
    12 : "C",
    13 : "D",
    14 : "E",
    15 : "F"
}

# def next():
#     yield n+1
# 진법 n, 
# 미리 구할 숫자의 갯수 t, 
# 게임에 참가하는 인원 m, 
# 튜브의 순서 p
def solution(n, t, m, p):
    for i in range(10):
        d[i] = str(i)
    # dict에 문자도 넣고 싶은데, 아스키 코드 구하는 함수를 모르겠다.
    
    # n진수 숫자 전체
    str_num = ""
    # n진법으로 변환할 숫자
    num = 0
    
    # n진법으로 나타낸 문자열 구하기
    # 숫자를 n으로 구한 나머지를 거꾸로 나열
    # m*t: 모든 인원이 말하는 것을 합쳤을 때의 문자열 길이 
    while len(str_num) < t*m:
        q, r = divmod(num, n)
        # num을 n진법으로 바꾼 수 (str)
        tmp = d[r]
        while q > 0:
            q, r = divmod(q, n)
            tmp = d[r]+tmp
            
        str_num += tmp
        num += 1

    
    # 튜브 순서 구하기
    # ~~~ for 루프로 구하기
    # answer = ''
    # for i in range(t):
    #     answer +=str_num[i*m+p-1]
    # return answer
    
    # ~~~ 슬라이싱으로 구하기
    return str_num[p-1:t*m:m]