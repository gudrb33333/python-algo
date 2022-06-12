import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

lists:list[ListNode] = [[1,4,5],[1,3,4],[2,6]]

root = result = ListNode(None)
heap = []

#각 연결리스트의 루트를 힙에 저장
for index in range(len(lists)):
    if lists[index]:
        heapq.heappush(heap, (lists[index].val, index, lists[index]))


print(heap)