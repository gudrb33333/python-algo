import collections


nums = [1,1,1,2,2,3]
k = 2

list(zip(*collections.Counter(nums).most_common(k)))[0]

#zip() 함수
a = [1,2,3,4,5]
b = [2,3,4,5]
c = [3,4,5]

