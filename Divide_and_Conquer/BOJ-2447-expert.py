# https://www.acmicpc.net/source/28199391


def concatenate(r1, r2):
    return [''.join(x) for x in zip(r1, r2, r1)]



def star10(n):
    if n == 1:
        return ['*']
    n //= 3
    x = star10(n)
    a = concatenate(x, x)
    b = concatenate(x, [' ' * n] * n)

    return a + b + a


# print('\n'.join(star10(int(input()))))

n3 = star10(3)
print(n3)

# 문자열 자체가 하나의 리스트처럼 작동
ar1 = ['123', 
        '456', 
        '789']
ar2 = ['abc', 
        'def', 
        'ghi']
ar3 = ['ABC', 
        'DEF', 
        'GHI']
print([x for x in zip(ar1, ar2, ar3)])
# [''.join(x) for x in zip(r1, r2, r1)]

print([''.join(x) for x in zip(ar1, ar2, ar3)])