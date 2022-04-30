ex_str_list:str = ['1 AA3 A','2 A C','3 AA1 A']



#split의 기본은 공백으로 나눔
print(ex_str_list[0].split())

print(ex_str_list[0].split()[1])

#람다 함수에서 먼저나온것 순으로 우선순위가 높음
ex_str_list.sort(key=lambda x: (x.split()[2], x.split()[1], x.split()[0]))

print(ex_str_list)

#내림차순
ex_str_list.sort(reverse=True, key=lambda x: (x.split()[2], x.split()[1], x.split()[0]))

print(ex_str_list)