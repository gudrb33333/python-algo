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
dist = collections.defaultdict(int)

for start, end ,take in times:
    graph[start].append((end, take))

Q = [(0,K)]

while Q:
    time, node = heapq.heappop(Q)
    if node not in dist:
        dist[node] = time
        for end, take in graph[node]:
            alt = time + take
            heapq.heappush(Q, (alt, end))

if len(dist) == N:
     print(max(dist.values()))