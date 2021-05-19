"""
https://leetcode.com/problems/majority-element/
2021.05.13
성공: correct

[아이디어]
Counter 모듈로 각 개체 개수 계산하고, 과반수가 넘는 것을 찾자.

[시간복잡도]
https://stackoverflow.com/questions/29240807/python-collections-counter-most-common-complexity/29240949

Counter 함수: O(n)
most_common: O(1)

따라서 O(n)

[개선/추가사항]
counter 모듈을 안 쓴다면..
카운트: 딕셔너리(숫자: 개수)
카운트 끝나면 순서쌍 heapify (-개수 기준): 최대힙으로 사용

heap에서 한번(최댓값을 꺼낸다) 숫자를 pop 한다.


"""

from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        

        count = Counter(nums)   # nums에서 각 개체가 몇 번 나오는지 카운트

#         for i in set(nums):
#             if count[i]>= (len(nums)+1)//2:
#                 return i

        # https://m.blog.naver.com/PostView.nhn?blogId=wideeyed&logNo=221540885097&proxyReferer=https:%2F%2Fwww.google.com%2F
        # count.most_common: 리스트 [(3, 2)]
        # count.most_common[]: 튜플 (3, 2)
        # count.most_common[][]: 원소 3
        return count.most_common(n = 1)[0][0]
        
        
        
