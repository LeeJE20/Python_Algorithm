'''idea
https://www.acmicpc.net/problem/1764


'''
import sys
import collections

read = sys.stdin.readline
print= sys.stdout.write

N, M = list(map(int, read().split()))

not_heard = [read().strip() for _ in range (N)]

result = []
for _ in range (M):
    not_seen = read().strip()
    if not_seen in not_heard:
        result.append(not_seen)

print(str(len(result))+'\n')
print('\n'.join(result))
