"""
https://leetcode.com/problems/group-anagrams/

49. Group Anagrams

난이도: Medium

시작: 21.09.23 11:04
끝: 21.05.11 12:13
성공: 1회 (예제는 5회)

메모리:  17.2 MB, less than 86.50%
시간:   96 ms, faster than 83.76%

[아이디어]
같은 anagram이면 정렬했을때 같은 단어가 된다.
defaultdict에 넣으면서 한다.


[시간복잡도]
O(n)


[실수]
1. split('')은 불가. (한 글자씩 자르기 불가)

a = 'hello'
print(a.split(""))
# ValueError: empty separator

한 글자씩 자르려면 list(str)을 해야 한다.

2. sort()는 그 자체를 정렬하고, sorted()는 정렬된 객체를 반환
-> 웬만하면 sorted를 사용하자.

3. 딕셔너리 keys()는 함수이다.


[검색]
https://wikidocs.net/21119
만약 문자열을 한 글자씩 나눠 저장하고 싶다면 다음과 같이 간단히 list로 Casting하기만 하면 된다.

>>> a = ‘hello’
>>> list(a)
[‘h’, ‘e’, ‘l’, ‘l’, ‘o’]


[개선/추가사항]
1. sorted(word)를 하면 문자열도 정렬 가능
2. dictionay.values()를 하면 값만 반환 가능

"""
import collections
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dd = collections.defaultdict(list)

        for word in strs:
            # key = ''.join(word.split("").sort())
            # key = ''.join(list(word).sort())

            # key = ''.join(sorted(word.split("")))
            key = ''.join(sorted(list(word)))
            dd[key].append(word)
        
        answer = []
        # keys = dd.keys
        # keys = list(dd.keys)
        keys = dd.keys()

        for k in keys:
            answer.append(dd[k])

        return answer

