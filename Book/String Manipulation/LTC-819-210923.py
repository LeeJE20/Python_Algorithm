"""
https://leetcode.com/problems/most-common-word/

819. Most Common Word

난이도: Easy

시작: 21.09.23 10:31
끝: 21.09.23 10:45
성공: 1회 시도

메모리:  14.2 MB, less than 73.01%
시간:   36 ms, faster than 73.85%

[아이디어]
1. 정규표현식으로 문자, 숫자만 남기기
2. 카운터 모듈로 개수 세기
3. banned에 없는 단어로 결과 도출


[시간복잡도]
count.most_common이 O(nlogn)이므로
O(nlogn)


[실수]



[검색]
https://wikidocs.net/4308
파이썬 정규표현식 사용법

파이썬 Counter 모듈 사용법 (개인 정리본)


[개선/추가사항]
정규표현식 부분을
paragraph = re.findall('[\w]+', paragraph.lower())
이렇게 해도 된다.




"""

import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 문자, 숫자만 골라내기
        # 반환값: 리스트
        p = re.compile('[\w]+')
        paragraph = p.findall(paragraph.lower())

        # 개수 헤아리기
        count = Counter(paragraph)
        common = count.most_common(n = len(count))

        # 금지된 단어에 있는 거면 다음 최다빈도 단어 선택
        i = 0
        while(common[i][0] in banned):
            i += 1

        # 최다 빈도 
        return common[i][0] 
