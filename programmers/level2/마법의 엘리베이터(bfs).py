import collections, heapq

def solution(storey):
    answer = 0
    
    storey_str_list = list(str(storey))    
    storey_int_list = list(map(int, storey_str_list))
    length = len(storey_str_list) - 1

    q = []
    heapq.heappush(q, (0, storey_int_list))

    while q:
        cost ,current_storey_list = heapq.heappop(q) 
        
        for index, value in enumerate(reversed(current_storey_list)):
            if value != 0:
                temp_current_storey_list = current_storey_list.copy()
                
                temp_current_storey_list[len(current_storey_list) - 1 - index] = 0
                temp_current_storey_list[len(current_storey_list) - 2 - index] += 1
                heapq.heappush(q, (10 - value + cost, temp_current_storey_list))
                
                temp_current_storey_list = current_storey_list.copy()
                temp_current_storey_list[len(current_storey_list) - 1 - index] = 0
                heapq.heappush(q, (value + cost, temp_current_storey_list))
                break
        
        result = 0
        for i in current_storey_list:
            result += i
        
        if result == 0:
            return cost
        
    return answer
