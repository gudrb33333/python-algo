import itertools, collections

def solution(n, info):
    answer = [0] * 11
    
    info_counter = collections.Counter()
    for index, i in enumerate(info):
        if i > 0:
            info_counter[10 - index] += i

    combi_key_list = itertools.combinations_with_replacement(range(0,11), n)
    
    combi_counter_list = []
    for combi_key in combi_key_list:
        combi_counter_list.append(collections.Counter(combi_key))

    temp_answer_counter = {}
    temp_result = 0
    for combi_counter in combi_counter_list:
        a_score = 0
        r_score = 0
        for i in range(0, 11):
            if info_counter[i] != 0 and info_counter[i] >= combi_counter[i]:
                a_score += i
            elif combi_counter[i] != 0:
                r_score += i
            
        if a_score - r_score < 0:
            if abs(a_score - r_score) > temp_result:
                temp_result = abs(a_score - r_score)
                temp_answer_counter = combi_counter

    if len(temp_answer_counter) == 0:
        return [-1]

    for i in temp_answer_counter:
        answer[10-i] = temp_answer_counter[i]
    
    return answer