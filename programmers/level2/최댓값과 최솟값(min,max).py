def solution(s):
    answer = ''
    
    s_list = s.split(' ')
    s_list = list(map(int,s_list))
    print(s_list)
    
    max_result = -1000000
    min_result = 1000000
    for s in s_list:
        max_result = max(s, max_result)
        min_result = min(s, min_result)
    
    return str(min_result) +" "+ str(max_result)
