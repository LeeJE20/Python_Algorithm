# https://leetcode.com/problems/most-common-word/
# 21.09.16



# 풀이1: 리스트 컴프리헨션, 카운터 객체 사용
# 입력값: 대소문자, 쉼표 등 구두점

import collections

def mostCommonWord(self, paragraph: str, banned: List[str])->str:
    # 정규식 처리
    # \w: 단어 문자
    # ^: not을 의미
    # 문자가 아닌 모든 문자를 공백으로 치환(subsitute)
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
            if word not in banned]

    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1

    # 딕셔너리 변수인 counts에서 값이 가장 큰 키를 가져온다
    return max(counts, key=counts.get)


# 풀이2: 카운터 모듈 사용
def mostCommonWord(self, paragraph: str, banned: List[str])->str:
    # 정규식 처리
    # \w: 단어 문자
    # ^: not을 의미
    # 문자가 아닌 모든 문자를 공백으로 치환(subsitute)
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
            if word not in banned]

    # 가장 흔하게 등학하는 단어의 첫 번째 인덱스 리턴
    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]

