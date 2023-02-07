import collections, heapq

def solution(book_time):
    answer = 0
    
    book_time.sort()
    book_end_time = []
    book_deque = collections.deque([])
        
    for book in book_time:    
        start_time_hour = int(book[0].split(':')[0])
        start_time_minute = int(book[0].split(':')[1])
        end_time_hour = int(book[1].split(':')[0])
        end_time_minute = int(book[1].split(':')[1])
        book_deque.append((60 * start_time_hour + start_time_minute, 60 * end_time_hour + end_time_minute + 10))

    time = 0
    while time != 1441:
        answer = max(answer, len(book_end_time))
        
        if len(book_deque) == 0:
            break
            
        if len(book_end_time) > 0:
            if book_end_time[0] == time:
                heapq.heappop(book_end_time)
        
        start_time = book_deque[0][0]        
        if start_time == time:
            book = book_deque.popleft()
            heapq.heappush(book_end_time, book[1])
        
        if len(book_deque) > 0:
            if book_deque[0][0] == time:
                continue
                
        if len(book_end_time) > 0:
            if book_end_time[0] == time:
                continue
                
        if start_time == time:
            continue
        time += 1
    
    return answer