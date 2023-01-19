def permutation(arr, visited, depth, temp):
    global result
    if depth == len(arr):
        temp_test = list(temp) 
        result.append(temp_test)

    for i in arr:
        if not visited[i - 1]:
            visited[i - 1] = True
            temp[depth] = i
            permutation(arr, visited, depth + 1, temp)
            visited[i - 1] = False

def solution(n, k):
    global result
    result = []
    answer = 0
    
    arr = []
    for i in range(n):
        arr.append(i+1)
    
    temp = [0 for i in range(n)]
    depth = 0
    visited = [False for i in range(n)]

    permutation(arr, visited, depth, temp)
    
    print(result)
    return answer