import pprint
import copy

a = [1, 2, 3]
b = a 
c = a[:]
d = a.copy()
e = copy.deepcopy(a)

f = []
f.append(a)

a.append(4)


#  'a': [1, 2, 3, 4],
#  'b': [1, 2, 3, 4],
#  'c': [1, 2, 3],
#  'd': [1, 2, 3],
#  'e': [1, 2, 3],
#  'f': [[1, 2, 3, 4]],



# 2차원 배열
fa = [1, [1, 2, 3], 2]
fb = fa # 전부 참조
fc = fa[:] # 2차원 부분이 참조
fd = fa.copy() # 2차원 부분이 참조
fe = copy.deepcopy(fa)

ff = []
ff.append(fa) # 전부 참조
fg = []
fg.append(copy.deepcopy(fa))

fa.append(4)
fa[1].append(4)
pprint.pprint(locals())


#  'fa': [1, [1, 2, 3, 4], 2, 4],
#  'fb': [1, [1, 2, 3, 4], 2, 4],
#  'fc': [1, [1, 2, 3, 4], 2],
#  'fd': [1, [1, 2, 3, 4], 2],
#  'fe': [1, [1, 2, 3], 2],
#  'ff': [[1, [1, 2, 3, 4], 2, 4]],



# 결론
# 1차원 배열의 복사
c = a[:]
d = a.copy()
e = copy.deepcopy(a)

# 2차원 배열의 복사
e = copy.deepcopy(a)