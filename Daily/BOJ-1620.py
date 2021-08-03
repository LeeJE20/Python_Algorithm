"""
https://www.acmicpc.net/problem/1620

나는야 포켓몬 마스터 이다솜

시작: 21.05.26 01:35
끝: 21.05.26 01:35
성공: correct

메모리: 51736 KB
시간:  296 ms

[아이디어]
딕셔너리 2개에 넣자.


[시간복잡도]
딕셔너리 구성: O(n)


[실수]
실수: input은 한 줄씩 읽어온다는 점을 간과했다.


[검색]
파이썬 map 리턴
https://dojang.io/mod/page/view.php?id=2286

[개선/추가사항]

# 고수 코드처럼 고쳐봤다..
# 메모리: 52848, 시간 236 ms

# 1. 입력은 N, T = map 어쩌구 이렇게 하는게 빠르다.
# 2. 딕셔너리보다 리스트가 빠르다
# 3. 중간중간에 print 하는 것보다 전부 묶어서 한 번만 print하는 것이 빠르다.



[고수풀이]
링크: https://www.acmicpc.net/source/22432446

메모리:52048  KB
시간:204   ms


접근법: ?? 나랑 똑같은데??


배울 점: 
n, m = map(int, input().split())
맵에 있는걸 리스트로 안 넣어도 불러올 수 있다.

https://codechacha.com/ko/python-string-strip/
strip()보다 rstrip이 빠르다.



코드
import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    pkmn = [] # 포켓몬 이름만
    pkmn_dic = {} # 이름, 번호 쌍
    res = []
    for i in range(1,n+1) :    
        pk = input().rstrip()
        pkmn.append(pk)
        pkmn_dic[pk] = i
    for _ in range(m):
        query = input().rstrip()
        if query.isdigit() :
            res.append(pkmn[int(query)-1])
        else :
            res.append(str(pkmn_dic[query]))
    print('\n'.join(res))
        
if __name__=='__main__':
    solve()


"""

import sys
input = sys.stdin.readline

# 실수: input은 한 줄씩 읽어온다는 점을 간과했다.
# arr = list(map(int, input().strip().split))
arr = list(map(int, input().split()))

N = arr[0]
T = arr[1]# 테스트 케이스 수

# print(f"{N}   {T}")

int_d = {}
str_d = {}

for i in range(1, N+1):
    name = input().strip()
    int_d[i] = name
    str_d[name] = i

for i in range(T):
    test = input().strip()
    if test.isdigit():
        print(int_d[int(test)])
    else:
        print(str_d[test])





# # 고수 코드처럼 고쳐봤다..
# # 메모리: 52848, 시간 236 ms

# # 1. 입력은 N, T = map 어쩌구 이렇게 하는게 빠르다.
# # 2. 딕셔너리보다 리스트가 빠르다
# # 3. 중간중간에 print 하는 것보다 전부 묶어서 한 번만 print하는 것이 빠르다.

# import sys
# input = sys.stdin.readline

# # 실수: input은 한 줄씩 읽어온다는 점을 간과하고, input을 2번 받음
# # arr = list(map(int, input().split()))

# # N = arr[0]
# # T = arr[1]# 테스트 케이스 수
# N, T = map(int, input().split())

# # int_d = {}
# int_d = []
# str_d = {}
# result = []

# for i in range(1, N+1):
#     # name = input().strip()
#     name = input().rstrip()
#     # int_d[i] = name
#     int_d.append(name)
#     str_d[name] = i

# for i in range(T):
#     # test = input().strip()
#     test = input().rstrip()
#     if test.isdigit():
#         result.append(int_d[int(test) -1])
#     else:
#         result.append(str(str_d[test]))

# print('\n'.join(result))
