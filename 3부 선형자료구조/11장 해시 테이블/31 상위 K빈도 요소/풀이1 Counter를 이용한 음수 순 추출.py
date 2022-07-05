nums = [1,1,1,2,2,3]
k = 2

freqs_heap = []
freqs = collections.Counter(nums)

for f in freqs:
    heapq.heappush(freqs_heap, (-freqs[f],f))

topk = []

for _ in range(k):
    topk.append(heapq.heappop(freqs_heap)[1])

print(topk)