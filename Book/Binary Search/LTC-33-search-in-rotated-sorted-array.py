#https://leetcode.com/problems/search-in-rotated-sorted-array/

"""내 풀이 아이디어

1. left와 right를 찾는다 (시작과 끝)

2.mid를 찾는다

3. left  <= mid  <= right 인지 확인

4-1. 처음으로 어긋나는 구간이 있으면
    그 구간으로 들어가서 1, 2, 3, 4 반복
4-2. 어긋나는 구간이 없으면: 0이 피벗
    

종료 조건: 배열의 길이가 3이하이다.
ㅍ
[2 0 1] : 첫 번쨰 구간에서 어긋나면 mid가 피벗
[1 2 0] : 두 번쨰 구간에서 어긋나면 right가 피벗


참고]
배열 길이가 2인 경우
(l, m, r = 0, 1, 1)
[0 1]: 어긋나는게 없으면 정렬된 배열
[1 0]: 첫 번째 구간에서 어긋났으므로 mid가 피벗

"""
