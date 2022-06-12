import collections

s:str = "cbacdcbc"

counter = collections.Counter(s)
strSet = set()
stack = []

for item in s:
    counter[item] -= 1
    if item in strSet:
        continue
    #뒤에 붙일 문자가 남아 있으면 스택에서 제거
    while stack and item < stack[-1] and counter[stack[-1]] > 0:
        strSet.remove(stack.pop())
    stack.append(item)
    strSet.add(item)

print(''.join(stack))        