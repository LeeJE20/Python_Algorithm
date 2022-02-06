'''idea
21.10.28

https://www.acmicpc.net/problem/9663
count = 0
def solve(board, left):
    if left == -1:
        count += 1
        return
    for i in range(N):
        if board[left][i]가 가능:
            board 안 되는 부분 표기 (가로, 세로, 대각선)
            solve(board, left - 1)

'''
import sys
import collections

read = sys.stdin.readline
print= sys.stdout.write

N = int(read())
arr = list(map(int, read().split()))

print(' '.join(map(str,arr)) + '\n')



        
