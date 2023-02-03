#그래프 bfs할때는
#1.방문여부 체크 visited = [False] * (n + 1)
#2.양방향 그래프인지 확인.
#   wire_dict = {}
#   for a, b in wires:
#       wire_dict[a] = b
#       wire_dict[b] = a
#3.queue를 활용.

import collections

def bfs(start_node, cut_node, wires_dict):

    count = 0
    visited = [False] * (len(wires_dict) + 1 )
    q = collections.deque([start_node])
    
    while q:
        current_node = q.popleft()
        if visited[current_node] == True:
            continue
        if cut_node == current_node:
            continue
            
        count += 1
        visited[current_node] = True
        next_node_list = wires_dict[current_node]
        
        for next_node in next_node_list:
            q.append(next_node)

    
    return count

def solution(n, wires):
    answer = 10000000

    wires_dict = collections.defaultdict(list)
    
    for a, b in wires:
        wires_dict[a].append(b)
        wires_dict[b].append(a)
    
    for v1, v2 in wires:
        value1 = bfs(v1, v2, wires_dict)
        value2 = bfs(v2, v1, wires_dict)
        diff = abs(value1 - value2)
        answer = min(answer, diff)

    return answer

wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
n = 9

solution(n, wires)