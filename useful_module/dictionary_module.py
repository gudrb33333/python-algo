import collections

print()

#defaultdict 객체
#기본값이 있는 딕셔너리 객체
defaultdict_a = collections.defaultdict(int)
defaultdict_a['A'] = 5
defaultdict_a['B'] = 6
#디폴트가 0이라 에러안나고 할당연산자 동작함
defaultdict_a['C'] += 1
print('defaultdict_a >>>>', defaultdict_a)
print()

#Counter 객체
#리스트에 있는 자료 갯수 딕셔너리로 반환
list_a:int = [1, 2, 3, 4, 5, 5, 5, 6, 6]
dict_a = collections.Counter(list_a)
print('dict_a_count >>>', dict_a)
print()

list_b:str = ['a', 'b', 'a', 'c', 'a', 'b']
dict_b = collections.Counter(list_b)
print('dict_a_count >>>', dict_b)
print()

#most_common()
#가장 많이 들어가 있는 자료 조회
print('dict_a_count >>>', dict_a.most_common(1))
print()
print('dict_b_count >>>', dict_b.most_common(2))
print()

#OrderedDict 객체
#딕셔너리의 순서를 유지해주는 객체
dict_c = collections.OrderedDict({'banana':3, 'apple':5, 'pear': 1})
print('OrderedDict_dict_c >>>', dict_c)