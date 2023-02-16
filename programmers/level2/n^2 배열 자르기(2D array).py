def solution(n, left, right):
    answer = []
    
    left_row = int(left/n)
    left_col = int(left%n)

    for _ in range(0, right - left + 1):
        if left_col > left_row:
            answer.append(left_col + 1)
        else:
            answer.append(left_row + 1)
        
        if left_col + 1 >= n:
            left_row += 1
            left_col = 0
        else:
            left_col += 1
    
    return answer
