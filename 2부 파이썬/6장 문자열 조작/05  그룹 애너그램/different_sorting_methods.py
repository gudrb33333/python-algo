from typing import *

#숫자정렬
a: List[int] = [2, 5, 1, 9 ,7]
print(sorted(a))

#문자정렬
b: List[int] = ['a', 'b', 'd', 'f', 'z']
print(sorted(b))
print("".join(sorted(b)))

#문자를 길이로 정렬
c: List[str] = ['ccc', 'aaaa', 'd', 'db']
print(sorted(c, key=len))

#key에 함수로 정렬
d = ['cde', 'cfc', 'cde']

def fn(s):
    return s[0],s[-1]

print(sorted(d, key=fn))

#람다를 이용

print(sorted(d, key=lambda x: (x[0], x[1])))
