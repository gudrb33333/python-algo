import collections
import heapq

times = [
    #출발, 도착, 시간
    [3,1,5],
    [3,2,2],
    [2,1,2],
    [3,4,1],
    [4,5,1],
    [5,6,1],
    [6,7,1],
    [7,8,1],
    [8,1,1]
]
N = 8
K = 3

graph = collections.defaultdict(list)

for u, v, w in times:
    graph[u].append((v,w))

#큐 변수: [(소요시간, 정점)]
Q = [(0,K)]
dist = collections.defaultdict(int)

#우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
while Q:
    time, node = heapq.heappop(Q)
    if node not in dist:
        dist[node] = time
        for v, w in graph[node]:
            alt = time + w
            heapq.heappush(Q, (alt, v))

if len(dist) == N:
     print(max(dist.values()))
print(-1)

    