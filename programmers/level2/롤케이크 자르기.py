import collections

def solution(topping):
    answer=0
    a = collections.Counter(topping)
    b = collections.Counter()
    
    for i in topping:
        a[i] -= 1
        b[i] += 1
        
        if a[i] == 0:
            a.pop(i)
        if len(a) == len(b):
            answer+=1
    
    return answer