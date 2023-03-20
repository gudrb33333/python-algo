def solution(n, s):
    if n > s:
        return [-1]

    base_number = int(s/n) 
    answer = [base_number] * n
    
    index = n - 1
    for i in range(0, s - (base_number * n)):
        answer[index] += 1
        
        index -= 1
        if index == -1:
            index = n - 1
        
    return answer
