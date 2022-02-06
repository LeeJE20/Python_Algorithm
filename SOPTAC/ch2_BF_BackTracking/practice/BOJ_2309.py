'''idea

'''
import sys
import collections

read = sys.stdin.readline
print= sys.stdout.write

N = int(read())
arr = list(map(int, read().split()))

print(' '.join(map(str,arr)) + '\n')


def solve(picked, target):
    if len(picked) >= 7:
