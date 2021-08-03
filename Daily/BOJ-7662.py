"""
https://www.acmicpc.net/problem/7662

이중 우선순위 큐

시작: 21.05.24 20:56
끝: 21.05.24 21:25
성공: wrong

메모리:  KB
시간:   ms

[아이디어]
프로그래머스에서 비슷한 문제 풀어본 적이 있다.
min heap과 max heap에 모두 더하고, size라는 변수를 관리해나가며 해결한다.
-> 확인해보니 예전에도 틀렸었다..
내가 예전에 틀리고 나서 이 사람 풀이를 보고 공부했었는데, 이 사람도 틀렸던건가..
https://dokylee.tistory.com/69
힘들다...




[시간복잡도]
O(nlogn)... 으로 하고 싶었다.

[실수]



[검색]
힙큐 삽입, 삭제


[개선/추가사항]
-> https://www.acmicpc.net/board/view/57305
이거나 보면서 공부하자. heap에서 중간에 있는 값을 삭제 가능한 방법이다.
항상 삭제 연산이 O(logn)이 된다.

배울 점: 삭제 연산이 있을 때, 삭제할 것들을 저장해두고 나중에 기회가 왔을 때 삭제하는 전략.
지금 삭제를 해야 한다고 바로 하지 않아도 되면, 나중에 해도 된다.
일의 우선순위를 생각해보자.


다른 사람 풀이중에 min값은 heap에서 pop하고, max는 그냥 리스트에서 max값을 찾아 pop한다.
이 경우 max의 pop은 O(n)이다.


[고수풀이]
링크: 

메모리:  KB
시간:   ms


접근법:


배울 점: 


코드



"""


import sys
input = sys.stdin.readline

import heapq
def solve():
    min_heap = []
    max_heap = []
    size = 0
    n = int(input())
    for i in range (n):
        command = list(input().rstrip().split())
        command[1] = int(command[1])
        
        if command[0] == "I":
            heapq.heappush(min_heap, command[1])
            heapq.heappush(max_heap, -command[1])
            size += 1
        # 최댓값 삭제
        elif size != 0  and command[0] == "D" and command[1] == 1:
            heapq.heappop(max_heap)
            size -= 1
        # 최솟값 삭제
        elif size != 0  and command[0] == "D" and command[1] == -1:
            heapq.heappop(min_heap)
            size -= 1
        
    # 출력단
    if size == 0:
        print("EMPTY")
    elif size == 1:
        print(str(min_heap[0])+ " " + str(min_heap[0]))
    else:
        print(f"{-(heapq.heappop(max_heap))} {heapq.heappop(min_heap)}")


N = int(input())
# arr = list(map(int, input().rstrip().split()))

for i in range(N):
    solve()