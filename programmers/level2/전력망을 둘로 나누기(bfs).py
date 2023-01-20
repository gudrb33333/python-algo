from collections import defaultdict, deque

#그래프 bfs할때는
#1.방문여부 체크 visited = [False] * (n + 1)
#2.양방향 그래프인지 확인.
#   wire_dict = {}
#   for a, b in wires:
#       wire_dict[a] = b
#       wire_dict[b] = a
#3.queue를 활용.

def bfs(start_point, cut_point, wires, n, wire_dict):
    count = 1
    visited = [False] * (n + 1)
    q = deque([start_point])
    visited[start_point] = True
    
    while q:
        p = q.popleft()
        for next_p in wire_dict[p]:
            if next_p == cut_point: continue
            if visited[next_p] is True: continue
            count += 1
            q.append(next_p)
            visited[next_p] = True
            
    return count

def solution(n, wires):
    answer = 100000
    # dictionary로 그래프 자료구조 저장
    wire_dict = defaultdict(set)
    for wire in wires:
        wire_dict[wire[0]].add(wire[1])
        wire_dict[wire[1]].add(wire[0])
    
    # wire 하나를 끊는 모든 경우의 수에 대해 bfs로 조사
    for wire in wires:
        v1 = wire[0]
        v2 = wire[1]
        a = bfs(v1, v2, wires, n, wire_dict) 
        b = bfs(v2, v1, wires, n, wire_dict)
        diff = abs(a - b)
        answer = min(diff, answer) # 두 전력망이 가지고 있는 송전탑 개수의 차이의 최소값 갱신
        
    return answer

wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
n = 9

solution(n, wires)