import collections

#TODO 리팩토링 하기

def solution(order):
    answer = 0
    
    i = 1
    container = collections.deque(order)
    sub_container = []    
    
    while True:
        if len(container) and container[0] == i:
            container.popleft()
            answer += 1
            i += 1
        elif len(sub_container) > 0 and len(container) > 0 and sub_container[-1] == container[0]:
            container.popleft()
            sub_container.pop()
            answer += 1
        else:
            if len(sub_container) > 0 and len(container) > 0 and sub_container[-1] > container[0]:
                break
            elif len(container) == 0 :
                break
            else:
                sub_container.append(i)
                i += 1

    
    return answer