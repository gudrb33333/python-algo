import heapq

def solution(operations):
    min_q = []
    max_q = []

    for operation in operations:
        operation_code = operation.split(" ")[0]
        operation_value = operation.split(" ")[1]
        
        if operation_code == "I":
            operation_value = int(operation_value)
            heapq.heappush(min_q, operation_value)
            heapq.heappush(max_q, -operation_value)
        elif len(min_q) > 0 and len(max_q) > 0 and operation_code == "D" and operation_value == "-1":
            min_value = heapq.heappop(min_q)
            max_q.remove(-min_value)
            
        elif len(max_q) > 0 and len(min_q) > 0 and operation_code == "D" and operation_value == "1":
            max_value = -heapq.heappop(max_q)
            min_q.remove(max_value)
    
    if len(min_q) == 0 or len(max_q) == 0:
        return [0,0]
    else:
        return [-max_q[0], min_q[0]]
