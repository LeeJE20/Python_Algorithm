# 21.11.19 10:41
# 21.11.19 11:31

# 인덱스 에러가 많았다.
"""
피드백

1. 문자열을 int로 바꾸는데, 10(2자리 수)을 문자 1개만 보고 1(1자리 수)로 처리함
    - 문제 조건이 몇 자리 수까지 있는지 보고, 자리수가 다양하면 이에 대응해야 함
2. while idx < len(dartResult): 에서 idx처리가 다 됐다고 생각했으나 

    for j in range(len(bonus)):
        if dartResult[idx]==bonus[j]:
            target[1] = j+1
            idx +=1

    블록에서 중간에 idx가 커치면 다음 for문에서 에러가 생긴다.

    - while문에서 중간중간에 조건의 idx가 커진다면, 
        idx가 커진 바로 다음 연산은 에러처리 할 것
    - while에서 for을 사용하고, for문 내부에서 idx가 커진다면,
        for문 내부에서도 idx처리가 필요함


[다른사람풀이]
https://programmers.co.kr/learn/courses/30/lessons/17682/solution_groups?language=python3#:~:text=15%0A16%0A17-,def,-solution(dartResult)%3A%0A%20%20%20%20dart

def solution(dartResult):
    dart = {'S':1, 'D':2, 'T':3}
    scores = []
    n = 0

    for i, d in enumerate(dartResult):
        if d in dart:
            scores.append(int(dartResult[n:i])**dart[d])
        if d == "*":
            scores[-2:] = [x*2 for x in scores[-2:]]
        if d == "#":
            scores[-1] = (-1)*scores[-1]
        if not (d.isnumeric()):
            n = i+1

    return sum(scores)

배울점
    1. 딕셔너리를 사용해 bonus를 for loop 없이 계산
    2. 점수, bonus, option을 따로 구하지 않고, 구하자마자 연산
    3. 포인트는 경우는 d.isnumeric()과 인덱스를 이용해 계산

"""
def solution(dartResult):
    bonus = ('S', 'D', 'T')
    option = ('*', '#')
    before_point, now_point = 0, 0
    target = [0, 0, 0]
    
    answer = 0
    
    idx = 0
    while idx < len(dartResult):
        target[0] = int(dartResult[idx])
        idx +=1
        # 실수: 점수가 10인 경우 처리         
        if dartResult[idx]=='0':
            target[0] = 10
            idx += 1
        for j in range(len(bonus)):
            if dartResult[idx]==bonus[j]:
                target[1] = j+1
                idx +=1
                # 실수: idx에러 방지 위해 break 처리
                break
        # 실수: 마지막에 option이 없는 경우를 위해 idx에러 검사   
        if (idx < len(dartResult)):
            for o in option:
                if dartResult[idx]==o:
                    target[2] = o
                    idx +=1
                    # 실수: idx에러 방지 위해 break 처리
                    break
        
        now_point = target[0]**target[1]
        
        # print(f"b, n = {before_point}, {now_point}")
        if target[2] == 0:
            # print(f"option 0")
            answer += now_point
        elif target[2] == '*':
            # print(f"option *")
            now_point *= 2
            answer += (before_point + now_point)
        elif target[2] == '#':
            # print(f"option #")
            now_point *= (-1)
            answer += now_point
        # print(answer)
        before_point = now_point
        target[2] = 0

    
    return answer

params = ["1S2D*3T", "1D2S#10S", "1D2S0T", "1S*2T*3S", "1D#2S*3S", "1T2D3D#", "1D2S3T*"]
ans = [37, 9, 3, 23, 5, -4, 59]
solution(params[1])
# for i in range(len(params)):
#     try:
#         print(f"\n\n~~~~~~~~~~~~case [{i}]")
#         res = solution(params[i])
#         if res == ans[i]:
#             print("맞음")
#         else:
#             print(f"틀림 result, answer = {res}, {ans[i]}")
#     except Exception as e:
#         print(e)