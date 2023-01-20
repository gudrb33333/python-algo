import collections
import heapq

#heapq를 쓸때는 우선순위를 요소를 맨 앞으로..
# ex> q=[]
# heapq.heappush(q, (0, 1))
#           총 걸린시간, 현재 마을
#
# 우선순위 큐를 사용해서 최소시간으로 갈 수 있는 최대한의 마을을 먼저 탐색한 후
# 나머지 시간을 활용하여 탐색
# 
# 우선순위 큐로 먼저 탐색한 후 이미 탐색한 곳은 continue 처리하여 최적화를 할 수 있음.

def bfs(N, road_dict, K):
    visited = [False] * (N + 1)

    q = []
    heapq.heappush(q, (0, 1))
    
    while q:
        currunt_village, time_sum = heapq.heappop(q)
        if visited[currunt_village] is True:
            continue
        visited[currunt_village] = True
        for next_village, time in road_dict[currunt_village]:
            if time_sum + time > K:
                continue
                
            heapq.heappush(q, (time_sum + time, next_village))

    visited_count = collections.Counter(visited)
    return visited_count[True]

def solution(N, road, K):
    road_dict = collections.defaultdict(list)
    for a, b, c in road:
        road_dict[a].append((b, c))
        road_dict[b].append((a, c))
    
    return bfs(N, road_dict, K)


road = 	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
N = 5
K = 3

print(solution(N, road, K))