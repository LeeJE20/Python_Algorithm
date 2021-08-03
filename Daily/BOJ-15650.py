"""
https://www.acmicpc.net/problem/15650

N과 M (2)

난이도: 실버 3

시작: 21.06.04 17:14
끝: 21.06.04 17:23
성공: 

메모리: 29200 KB
시간:  72 ms

[아이디어]
재귀로 풀면 되겠다.





[시간복잡도]
모르겠다.


[실수]



[검색]



[개선/추가사항]
sys.stdout.write를 쓰면 print보다 빠르다.


[고수풀이]
링크: https://www.acmicpc.net/source/17377227

메모리: 29284 KB
시간:  52 ms


접근법: 나랑 똑같은데 왜 나는 느리지?


배울 점: 


코드



"""


def solve_recursion():

    # 출력 함수를 바꿨다.
    # 4ms 더 빨라졌다...
    import sys
    input = sys.stdin.readline


    N, M = map(int, input().split())


    # 아이디어: 작은 숫자부터 뽑는다. 한 숫자를 선택한 뒤, 이것보다 큰 수들 중에서 하나를 뽑는다.

    # picked: 뽑은 것들
    # toPick: 더 뽑아야 하는 것 개수
    # nowNum: 방금 추가된 숫자
    def solve(picked: list,  toPick: int, nowNum: int):
        if toPick == 0:
            # print(' '.join(map(str, picked)))
            sys.stdout.write(" ".join(map(str,picked)) + "\n")
            return

        for i in range(nowNum+1, N+1):
            picked.append(i)
            solve(picked, toPick-1, i)
            picked.pop()

    picked = []

    solve(picked, M, 0)




# # 위와 같은 아이디어를 스택으로 구현해본다.
# # 근데 잘 모르겠다.
# # for문을 어떻게 while에 끼워넣지? 재귀 부분을 어떻게 할까..
# def solve_stack():
#     import sys
#     input = sys.stdin.readline


#     N, M = map(int, input().split())

#     from collections import deque    
#     picked = [0] * M

#     d = deque()

#     toPick = M
#     nowNum = 0
#     for i in range(1, N+1):
#         d.append(i)
#         toPick -= 1

#         while d:
#             for i in range(nowNum+1, N+1):
#                 if (toPick == 0):
#                     print(' '.join(map(str, picked)))
#                     toPick += 1
                

            


# 고수 풀이를 보고 개선시켜 보았다.
# def solve2():
# 음,, solve 파라미터로 picked가 들어가야 더 빠르다!!



# 출력 함수를 바꿨다.
# 4ms 더 빨라졌다...
# import sys
# input = sys.stdin.readline


# N, M = map(int, input().split())

# num = [i for i in range(1, N+1)]

# picked = []
# # 아이디어: 작은 숫자부터 뽑는다. 한 숫자를 선택한 뒤, 이것보다 큰 수들 중에서 하나를 뽑는다.

# # picked: 뽑은 것들
# # toPick: 더 뽑아야 하는 것 개수
# # nowNum: 방금 추가된 숫자
# def solve(picked: list, toPick: int, nowNum: int):
#     if toPick == 0:
#         # print(' '.join(map(str, picked)))
#         sys.stdout.write(" ".join(map(str,picked)) + "\n")
#         return

#     for i in range(nowNum+1, N+1):
#         picked.append(i)
#         solve(picked, toPick-1, i)
#         picked.pop()



# solve(picked, M, 0)

