# https://leetcode.com/problems/reorder-data-in-log-files/
# 21.09.14

# 풀이1: 람다와 + 연산자를 이용

# 요구조건을 얼마나 깔끔하게 처리할 수 있는지를 묻는 문제
# 문자와 숫자를 구별하고 숫자는 나중에 그대로 이어붙인다
def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 2개 키를 람다 표현식으로 정렬
    # 식별자를 재외한 문자열 [1:]을 키로 하여 정렬하여, 
    # 동일한 경우 후순위로 식별자 [0]를 지정해 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letters + digits