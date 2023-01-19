import collections
import heapq

dict = collections.defaultdict(list)
dict['테스트'].append(('일',1))
dict['테스트'].append(('이',2))
dict['테스트'].append(('삼',4))
dict['테스트'].append(('튜플',(3,1,2)))

print(dict)
print(len(dict))
print(len(dict['테스트']))
print(len(dict['테스트'][3][1]))

print('-------------------------------')
for a, b in dict['테스트']:
    print(a) #일
    print(b) #1

dict2 = collections.defaultdict(int)
dict2['test'] # 0

print('-------------------------------')
print('deq')
deq = collections.deque()

deq.append(1)
deq.append(2)
deq.appendleft(3)

print( deq.popleft())
print( deq.pop())

print('-------------------------------')
print('heapq: 최소힙')
heap_items = [3,2,1,4,5]
heapq.heapify(heap_items)
heapq.heappush(heap_items,8)

print(heapq.heappop(heap_items))

print('heapq:최대힙')
max_heap = []
for item in heap_items:
    heapq.heappush(max_heap, (-item, item))

print(heapq.heappop(max_heap)[1])

print('-------------------------------')
print('set')   
s1 = set({1, 2, 3})
s1.add(1)
s1.add(4)
print(s1)
s1.remove(3)

print(s1)
print(len(s1))

ex_str_list:str = ['1 AA3 A','2 A C','3 AA1 A']

print('-------------------------------')
print('sort')   
#split의 기본은 공백으로 나눔
print(ex_str_list[0].split())

print(ex_str_list[0].split()[1])

#람다 함수에서 먼저나온것 순으로 우선순위가 높음
ex_str_list.sort(key=lambda x: (x.split()[2], x.split()[1], x.split()[0]))

print(ex_str_list)

#내림차순
ex_str_list.sort(reverse=True, key=lambda x: (x.split()[2], x.split()[1], x.split()[0]))

print(ex_str_list)

#빈배열 만들기
list = [0 for i in range(3)]
matrix = [[0 for col in range(3)] for row in range(3)]