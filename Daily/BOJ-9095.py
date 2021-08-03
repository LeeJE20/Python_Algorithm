"""
https://www.acmicpc.net/problem/9095
1, 2, 3 더하기

시작: 21.05.22 12:18
끝: 21.05.22 12:46
성공: correct

메모리: 31924, 시간 108

[아이디어]
이번에야말로 브루트포스!..는 시간초과 날지도..


음 근데 얘도 dp로 할 수 있겠다!

solve(n)의 리턴:n을 1, 2, 3의 합으로 나타내는 방법의 수

solve(n)은

solve(n-1)
solve(n-2)
solve(n-3)
의 합이다.

이유: n-1을 만드는 각각의 방식에 +1만 추가하면 n을 만들 수 있다.
마찬가지로 n-2, n-3을 만드는 각각의 방식에 +2, +3만 추가하면 n을 만들 수 있다.
예)
solve(1) = 1
solve(2) = 2
    1+1
    2
solve(3) = 4
    1+1+1
    1+2
    2+1
    3

solve(4) = 7
[solve(n-1)]의 측면
    1+1+1   +1
    1+2     +1
    2+1     +1
    3       +1
[solve(n-2)]의 측면
    1+1     +2
    2       +2
[solve(n-3)]의 측면
    1 + 3

아이디어끝 시간: 12: 28

[시간복잡도]
배열을 한 번만 훑으면 된다. O(n)


[실수]
for 코드 복붙할 때 

for i in range(n):
    n = 어쩌구

위처럼 내부에서 i에 관한 것이 아닌 n에 관한 것을 작성한다.
for문을 복붙하면 코드가 꼬이지 않게 변수 확인을 잘 하자.

[검색]


[개선/추가사항]
메모이제이션은 재귀 돌고, 타뷸레이션은 for문으로 처리해서 
타뷸레이션이 더 빠를 줄 알았는데 메모이제이션이 더 빨랐다. 이유가 뭘까..


고수풀이]
나랑 접근법은 같다. 함수를 따로 사용하지 않아 더 빠르다.
메모리: 29284, 시간 52
N = int(input())
arr=[1,2,4]
for i in range(4,11):
    arr.append(sum(arr[-3:]))
for _ in range(N):
    T = int(input())
    print(arr[T-1])

고수풀이2]
import sys

# 앞부분만 숫자 넣고 나머지 0으로 초기화하는 부분
m=[0,1,2,4]+[0 for i in range(7)]
for i in range(4, 11):
    m[i]=sum(m[i-3:i])
_,*i=map(int,sys.stdin.readlines())
for i in i:
    print(m[i])


"""

from collections import defaultdict
global dic


def solve(n: int)-> int:
    # 메모이제이션
    # 메모리 32752, 시간 96
    
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    global dic

    if dic[n] != 0:
        return dic[n]
    
    dic[n] = solve(n-1) + solve(n-2) + solve(n-3)
    return dic[n]



global arr
arr = [0 for _ in range(11)]

def memoization_list(n: int)-> int:
    # 메모이제이션 (딕셔너리 말고 리스트 사용)
    # 메모리 32752, 시간 96
    # 결론: 딕셔너리쓰든 리스트 쓰든 메모리나 시간은 같다.
    
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    global arr

    if arr[n] != 0:
        return arr[n]
    
    arr[n] = memoization_list(n-1) + memoization_list(n-2) + memoization_list(n-3)
    return arr[n]


def solve2(n: int)-> int:
    # 타뷸레이션
    # 메모리 32048, 시간 100


    if dic[n] != 0:
        # print(f"dic[n] = {dic[n]}")
        return dic[n]

    
    for i in range(4, n+1):
        dic[i] = dic[i-1] + dic[i-2] + dic[i-3]
        # print(f"dic[i] = {dic[i]}")
    return dic[n]
    
    






import sys
input = sys.stdin.readline
# 딕셔너리 초기화
dic = defaultdict(int)
N = int(input())

# 타뷸레이션 초기화
dic[1]= 1
dic[2]= 2
dic[3]= 4

for i in range(N):
    # 메모이제이션
    print(solve(int(input())))

    # 메모이제이션_ 리스트
    # print(memoization_list(int(input())))

    # 타뷸레이션
    # print(solve2(int(input())))

