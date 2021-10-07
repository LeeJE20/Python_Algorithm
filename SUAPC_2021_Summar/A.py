'''idea

'''



# def solution(boxnum, velocity):
#     # answer = 0
#     a_heap = []
#         # a 팀
        
#     for v in velocity:
#         heapq.heappush(a_heap, v)
    
#     b_MIN_v = heapq.heappop(a_heap)
#     b_cnt = 1
		
#     MIN_TIME = math.ceil(boxnum / (b_cnt*b_MIN_v + a_heap[0]*len(a_heap)))

#     # MIN_TIME = boxnum *(1//(1*b_MIN_v) + 1//a_heap[0])
#     while(len(a_heap) > 1):
#         heapq.heappop(a_heap)
#         b_cnt += 1
#         # b_MIN_v = min(b_new, b_MIN_v)
#         this_time = math.ceil(boxnum / (b_cnt*b_MIN_v + a_heap[0]*len(a_heap)))
#         MIN_TIME = min(this_time, MIN_TIME)

#         # print(b_MIN_v, a_heap, this_time, MIN_TIME)
        

#     return MIN_TIME
# import pprint

"""
10만큼의 일이 있다.
A의 작업속도는 11, b는 9라면..

1분만 더 작업하면 됨.


"""

import sys; read = sys.stdin.readline
import heapq
import math

def solution(boxnum, velocity):
    velocity.sort()
    
    b_MIN_v = velocity[0]
    b_cnt = 0

    a_MIN_v = -1
    a_cnt = N
	
    max_vel = -1
    for i in range(1, N):

        b_cnt += 1

        a_MIN_v = velocity[i]
        a_cnt -= 1

        # now = b_cnt*b_MIN_v + a_cnt*a_MIN_v
        
        max_vel = max(max_vel, b_cnt*b_MIN_v + a_cnt*a_MIN_v)
        # pprint.pprint(locals())

    return math.ceil(boxnum /max_vel)

N, K = list(map(int, read()[:-1].split(' ')))
velocity = list(map(int, read()[:-1].split(' ')))

print(solution(K, velocity))