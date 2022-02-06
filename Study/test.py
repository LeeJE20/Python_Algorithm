from typing import DefaultDict


d = {"a": 1, "b":0}

print(d.get("a")) # 1
print("a" in d) # True

print(d.get("b")) # 0
print("b" in d) # True

print(d.get("c")) # None
print("c" in d) # False

# * * 주의: if 안에 그냥 get을 쓰면 value에 따라 False 나올 수 있다.
if (d.get("b")):
    print("b 있음")
else:
    print("b 없음") # 여기가 실행됨

# 이렇게 None이 아니다로 명시하는 것이 안전
if (d.get("b") != None):
    print("b는 None이 아님")

Defa = 1

