import collections, itertools, bisect

def solution(info, query):
    answer = []
    
    info_dict = collections.defaultdict(list)
    
    # 0,1,2,3의 모든 조합 뽑기
    comb_key = []
    for i in range(1,5):
        comb_key.extend(itertools.combinations(range(0,4), i))
    
    #조건에 맞게 딕셔너리 만들기
    for i in info:
        info_condition_list = i.split()
        info_condition = info_condition_list[:-1]
        score = int(info_condition_list[-1])
        info_dict[' '.join(info_condition)].append(score)
        for key in comb_key:
            info_condition_temp = info_condition.copy()
            for v in key:
                info_condition_temp[v] = '-'
            
            info_dict[' '.join(info_condition_temp)].append(score)

    for i in info_dict:
        info_dict[i].sort()
    
    for q in query:
        query_list = q.split(' ')
        query_key = ''
        
        for index, i in enumerate(query_list):
            if index == len(query_list)-2:
                query_key += i
                break
            if index%2 == 0:
               query_key += i + ' '
        
        score = int(query_list[-1])

        #bisect로 스코어 이상인 값 갯수 추하기
        if len(info_dict[query_key]) > 0:
            idx = bisect.bisect_left(info_dict[query_key], score)
            answer.append(len(info_dict[query_key]) - idx)
        else:
            answer.append(0)

    return answer