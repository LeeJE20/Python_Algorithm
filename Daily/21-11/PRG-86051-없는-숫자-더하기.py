'''idea
https://programmers.co.kr/learn/courses/30/lessons/86051
1단계
21.11.06
풀이 시간: 5분 이내
시도 횟수: 1회
'''
def solution(numbers):
    exist = [0 for i in range(10)]
    answer = 45
    for i in numbers:
        if exist[i] == 0:
            exist[i] = 1
            answer -= i
    return answer