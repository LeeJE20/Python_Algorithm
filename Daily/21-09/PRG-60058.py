"""
https://programmers.co.kr/learn/courses/30/lessons/60058

괄호 변환

난이도: level 2

시작: 21.09.06 
끝: 21.09.06 

소요 시간: 34분 30초 걸림

성공: test case 시도 3회, 제출 1회 성공 

메모리:  KB
시간:   ms

[아이디어]



[시간복잡도]



[실수]



[검색]



[개선/추가사항]



[고수풀이]
링크: https://programmers.co.kr/learn/courses/30/lessons/60058/solution_groups?language=python3

메모리:  KB
시간:   ms


접근법:


배울 점: 
람다를 잘 쓴다.


코드
def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))


"""


"""
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
    단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.

"""




def balance(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
    if p == "":
        return ""

    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 
    idx = 0
    count = 0

    if p[idx] == '(':
        count += 1
    else:
        count -= 1
    idx += 1

    # 올바른 괄호 문자열인지
    # 실수: )(인 경우, if 이하를 안 붙이면 마지막에 correct = true가 된다.
    correct = True if count > 0 else False

    # 균형잡힌 괄호 문자열 부분 추출
    # count가 0이 되면 빠져나옴
    while count != 0:
        if p[idx] == '(':
            count += 1
        else:
            count -= 1
        if count < 0:
            correct = False
        idx += 1
    # idx는 v의 시작 인덱스가 된다.
    u = p[:idx]

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    if correct:
        #   3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
        return u+balance(p[idx:])
    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
    else:
        # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
        # 4-3. ')'를 다시 붙입니다. 
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        # 4-5. 생성된 문자열을 반환합니다.
        tmp = "("
        tmp += balance(p[idx:])
        tmp += ")"
        u = u[1:-1]
        for i in u:
            if i == "(":
                tmp += ")"
            else:
                tmp += "("
        return tmp


def solution(p):
    if p == "":
        return ""

    return balance(p)
