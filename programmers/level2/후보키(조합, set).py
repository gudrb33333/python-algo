import itertools

def solution(relation):
    row_len = len(relation)
    col_len = len(relation[0])
    
    combination_keys = []
    for i in range(1, 1 + col_len):
        combination_keys.extend(itertools.combinations(range(col_len), i))
    
    candidate_key = []
    for key in combination_keys:
        temp = set()
        for row in relation:
            temp.add(tuple(row[i] for i in key))
        if len(temp) == row_len:
            candidate_key.append(key)
            
    answer = set(candidate_key)
              
    for i in range(len(candidate_key)):
        a = set(candidate_key[i])
        for j in range(i + 1, len(candidate_key)):
            b = set(candidate_key[j])
            if a.intersection(b) == a:
                answer.discard(candidate_key[j])
        
    return len(answer)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

solution(relation)