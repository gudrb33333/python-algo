import collections, heapq

def solution(k, tangerine):
    answer = 0
    
    tangerine_counter = collections.Counter(tangerine)
   
    q = []
    for key, value in tangerine_counter.items():
        heapq.heappush(q, -value)
    
    while k > 0:
        value = abs(heapq.heappop(q))
        k -= value
        answer += 1
    
    return answer
