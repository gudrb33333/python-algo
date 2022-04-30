
import collections
from typing import *

#문자열 배열을 받아 애너그램 단위로 그룹핑하라

#입력
ex_str_list: List[str] = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = collections.defaultdict(list)

for ex_str in ex_str_list:
    anagrams[''.join(sorted(ex_str))].append(ex_str)

print(anagrams)


