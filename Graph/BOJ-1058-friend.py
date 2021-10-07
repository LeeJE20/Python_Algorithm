"""
https://www.acmicpc.net/problem/1058

친구

난이도: 실버 2

시작: 21.08.23 23:04
끝: 21.08.23 23:36
성공: 포기

메모리:  KB
시간:   ms

[아이디어]
노드의 2칸이 가장 많은 노드를 출력하기.

각 노드의 연결된 것들의 개수 헤아린다.

0 - 1, 2
1 - 0, 2
2 - 0, 1


음 모르겠다...

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

# import sys
# input = sys.stdin.readline
# print = sys.stdout.write

N = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]
for j in range(N):
    txt = input()
    for i in range(N):
        if txt[i] == "Y":
            arr[j][i] = 1

print(" ".join(map(str,arr)) + "\n")


