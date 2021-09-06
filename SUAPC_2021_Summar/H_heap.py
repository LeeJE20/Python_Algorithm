'''idea

'''
import sys
import collections

read = sys.stdin.readline
out= sys.stdout.write

import heapq

h = []

def insert(num):
    heapq.heappush(h, num)

def pop_max():
    return h.pop(h.index(heapq.nlargest(1, h)[0]))
    
def pop_min():
    return heapq.heappop(h)



N, X = list(map(int, read().split()))
C = list(map(int, read().split()))

for i in C:
    insert(i)
half = X/2
result = 0
while len(h)>1:
    # print(str(len(h)))
    maxC = pop_max()
    # print("pop max: " +str(maxC))
    # max가 이미 꽉 차있다면 개수 하나 추가
    if maxC >= X:
        result+= 1
        continue

    minC = pop_min()

    new = min(X, maxC+minC+half)

    # print(f"M, m, n, size = {maxC}, {minC}, {new}, {len(h)}")
    # 새로 받은 용기가 꽉 차있으면
    if new >= X:
        
        result+= 1
        # print(f"result++: {result}")
        continue
    # 새로 받은 용기가 꽉 안 차있으면
    else:
        # print(f"insert ${new}")
        insert(new)


out(str(result))
# print("끝")


