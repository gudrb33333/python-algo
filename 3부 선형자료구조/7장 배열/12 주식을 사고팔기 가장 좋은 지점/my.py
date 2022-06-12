#한번의 거래로 낼 수 있는 최대 이익을 산출하라.

nums: list[int] = [7, 1, 5 ,3 ,6, 4]

my_dict = dict() 
for index,value in enumerate(nums):
  my_dict[value] = index

my_dict = sorted(my_dict.items())



print(my_dict[0])
print(my_dict[len(my_dict)])



