"""
https://programmers.co.kr/learn/courses/30/lessons/67256

[카카오 인턴] 키패드 누르기

난이도: level1

시작: 21.10.08 10:19
끝: 21.10.08 11: 53
성공: 

메모리:  KB
시간:   ms

[아이디어]
왼손 위치, 오른손 위치 기억

딕셔너리에 가운데-가장자리 거리 기록해두고, 거기서 뽑아 쓰자

규칙(가장자리, 가운데 거리)
    1. 1차이나는 숫자는 1칸 차이난다. 
        - 0, 1 제외
    2. 4차이나는 숫자는 2칸 차이
        - 0, 4 제외
    3. 0과 8은 1 차이난다.

아이디어2: 동적으로 계산
규칙:
    가운데숫자 - 왼쪽숫자, 가운데숫자 - 오른쪽숫자 -2 중 작은 값으로 계산
    

아이디어3: 2, 5, 8, 0만 거리 계산
    1. 0은 11으로 처리
    2. left, right가 가운데에 있을떄는 n - 위치
    3. left, right가 사이드에 있을 때는 n - (사이드에서 가운데 위치로 옮김) + 1칸

[시간복잡도]



[실수]



[검색]



[개선/추가사항]



[고수풀이]
링크: 

메모리:  KB
시간:   ms


접근법:


배울 점: 


코드



"""

def get_distance():
    dic = {2:{}, 5:{} ,8:{}, 11:{}}
    for n in [2, 5, 8, 11]:
        for i in range(1, 13):
            d = abs(n - i) // 3
            if i in [3, 6, 9, 12]:
                d = (abs(n - (i - 1)) + 3)//3
            if i in [1,4,7,10]:
                d = (abs(n - (i + 1)) + 3)//3
            dic[n][i] = d
    # for k in dic.keys():
    #     print(f"{k}: {dic[k]}")
    return dic

def solution(numbers, hand):
    answer = ''
    left, right = 10, 12

    distance = get_distance()
    for n in numbers:
        if n in [1, 4, 7]:
            left = n
            answer += 'L'
        elif n in [3, 6, 9]:
            right = n
            answer += 'R'
        else:
            if n == 0:
                n = 11
            left_distance = distance[n][left]
            # right_distance = n - right - 2
            right_distance = distance[n][right]
            # if right in [3, 6, 9]:
            #     right_distance = abs(n - (right - 1)) + 3
            # if left in [1,4,7]:
            #     left_distance = abs(n - (left + 1)) + 3

            # if left == 0 and n != 0:
            #     left_distance = abs(n - 11)
            # if right == 0 and n != 0:
            #     right_distance = abs(n - 11)
            
            if left_distance==right_distance:
                if hand == 'left':
                    left = n
                    answer += 'L'
                else:
                    right = n
                    answer += 'R'
            elif left_distance < right_distance:
                left = n
                answer += 'L'
            else:
                right = n
                answer += 'R'
        # print(f"n: l, r, ans = {n}: {left}, {right}, {answer}")

    return answer


# solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5])


