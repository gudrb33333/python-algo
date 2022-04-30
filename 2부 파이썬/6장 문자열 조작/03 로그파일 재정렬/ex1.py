#로그를 재정렬하라
# 1. 로그의 가장 앞 부분은 식별자다.
# 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
# 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
# 4. 숫자 로그는 입력 순서대로 한다.

from typing import *

logs:str = ["dig1 8 1 5 1","let1 art can","dig2 3 6", "let2 own kit dig", "let3 art zero"]

def reorderLogFiles(logs: List[str]) -> List[str]:
    letter_str_list: List[str] = [] 
    digits_str_list: List[str] = []
    
    for log in logs:
        if log.split()[1].isdigit():
            digits_str_list.append(log)
        else:
            letter_str_list.append(log)

    letter_str_list.sort(key= lambda x: (x.split()[1:], x.split()[0]))    

    return letter_str_list + digits_str_list

print(reorderLogFiles(logs))