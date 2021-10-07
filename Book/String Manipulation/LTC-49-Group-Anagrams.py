# https://leetcode.com/problems/group-anagrams/
# 그룹 애너그램
# 21.09.17

"""
내 아이디어

단어마다 정렬하고, 키 값과 같은지 확인
defaultdict += 1
"""

# 풀이1: 정렬하여 딕셔너리에 추가
import collections

def groupAnagrams(self, strs: List[str])->List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())