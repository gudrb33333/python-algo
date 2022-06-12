temperatures = [73,74,75,71,69,72,76,73]

answer = [0] * len(temperatures)
stack = []

for index, item in enumerate(temperatures):
    #현재 온도가 스택값 보다 높다면 정답 처리
    while stack and item > temperatures[stack[-1]]:
        last = stack.pop()
        answer[last] = index - last
    stack.append(index)

print(answer)