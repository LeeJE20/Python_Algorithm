'''idea
틀림

연산??
start=(N+K)- (2*K)
(씨그마 i = (N+K)- (2*K)부터 N까지의 합)* 4

 (N+K)- (2*K)가 음수면 1부터 N까지의 합으로 처리

n = start 
최종 연산: N(N + 1) / 2 - (n-1)n/2




sum = N
earth = N
for i in range K:
    earth = earth + 1
    sum 



'''
import sys
# import collections

read = sys.stdin.readline
print= sys.stdout.write

T = int(read())

def solve():
    N, K = list(map(int, read().split()))
    start=(N+K)- (2*K)
    if start < 0:
        start = 1
    print( str( int((N*(N + 1)) / 2 - ((start-1)*start)/2)*4))


for _ in range(T):
    solve()