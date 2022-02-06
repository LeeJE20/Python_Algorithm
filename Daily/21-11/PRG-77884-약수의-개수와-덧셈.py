"""
https://programmers.co.kr/learn/courses/30/lessons/77884

월간 코드 챌린지 시즌2
약수의 개수와 덧셈

level 1

21.11.12
30분 내 풀이

[문제 유형]
구현

[몰랐던 문법]

[접근 방향]
모든 수를 더하고, 약수의 개수가 홀수인 수를 뺀다.
제곱수는 약수의 개수가 홀수이다.

[실수]
1. 모든 수를 더하고, 약수의 개수가 홀수인 수를 그냥 빼면
약수의 개수가 짝수인 수만 더한 꼴이다.
약수의 개수가 홀수인 수를 빼려면 *2를 하여 빼야 한다.

2. 1~n까지의 합은 (n*(n+1)) // 2이다.
따라서 left


[문제에서 배울 점]
문제가 수들을 덧셈하거나 뺄셈하는 문제일 때
모든 수를 더하고 특정 조건 숫자를 뺄셈하는 식으로 접근하면
뺄셈할 때 *2 해서 빼야 함.
"""

import bisect
def solution(left, right):
    # 약수의 개수가 홀수이려면 제곱수이다.
    # [1, 1000] 사이의 제곱수
    target = [ i**2 for i in range(1, int(1000**(1/2))+1)]
    # [left, right] 모든 수의 합
    answer = (right* (right+1))//2 - (left*(left-1))//2
    # answer = sum(range(left, right+1))
    
    left_idx = bisect.bisect_left(target, left)
    right_idx = bisect.bisect_right(target, right)
    
    for i in range(left_idx, right_idx):
        # 이미 모든 수를 더했으므로 *2 해서 빼야 함
        answer-= (target[i]*2)
        
    return answer

           
