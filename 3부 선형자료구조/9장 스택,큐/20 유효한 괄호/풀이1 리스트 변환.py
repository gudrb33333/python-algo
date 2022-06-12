#괄호로 된 입력값이 올바른지 판별해라

from turtle import st


s = "[({)}]"

stack = []
table = {
    ')': '(',
    '}': '{',
    ']': '[',
}

#스택 이용 예외 처리 및 일치 여부 판별
for char in s:
    if char not in table:
        stack.append(char)
    elif not stack or table[char] != stack.pop():
        print(False)
print(len(stack) == 0)