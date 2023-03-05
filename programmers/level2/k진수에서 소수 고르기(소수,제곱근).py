import collections

def isPrime(n):
    if n == 1:
        return False
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            return False
    return True             # n == 2 or 3 일때 소수지만 range를 만족하지는 않음

def solution(n, k):
    answer = 0

    q = collections.deque([])
    while n/k > 0:
        q.appendleft(str(n%k))
        n = int(n/k)

    temp_arr = []
    for i in q:
        if int(i) > 0:
            temp_arr.append(i)
        elif len(temp_arr) > 0:
            value = int(''.join(temp_arr))
            if isPrime(value):
                answer += 1
            
            temp_arr = []
    
    if len(temp_arr) > 0:
        value = int(''.join(temp_arr))
        if isPrime(value):
            answer += 1
    
    return answer
