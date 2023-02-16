import collections

def solution(s):
    answer = 0
    
    s_table = {
        '}':'{',
        ')':'(',
        ']':'['
    }
    
    s = collections.deque(s)
    for index in range(0,len(s)):
        if index != 0:
            tem_s = s.popleft()
            s.append(tem_s)
            
        s_stack = []
        for item in s:
            if len(s_stack) == 0:
                s_stack.append(item)
            else:
                if item == '}' or item == ']' or item == ')':
                    if s_stack[len(s_stack)-1] == s_table[item]:
                        s_stack.pop()
                    else:
                        s_stack.append(item)
                else:
                    s_stack.append(item)
        if len(s_stack) == 0:
            answer += 1
    
    return answer
