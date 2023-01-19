#금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 
#대소문자 구분을 하지 않으며,구두점(마침표,쉼표) 또한 무시한다

from typing import *
import collections
import re
 
#입력
paragraph: str = "Bob hit a ball, the hit BALL flew far after it was hit."
banned: List[str] = ["hit","ball"]

lower_paragraph: str = paragraph.lower()
#정규식에서 ^은 not을 의미... -> re.sub('[^a-z\s]','',lower_paragraph)
#a-z와 \s(스페이스) 아닌것은(^) ''처리 
#^\w 는 문자아닌것
fixed_paragraph: str = re.sub('[^\w]',' ',lower_paragraph)
fixed_paragraph_list: List[str] = fixed_paragraph.split()

print(fixed_paragraph_list)

dict = collections.defaultdic(int)
for item in fixed_paragraph_list:
    if item not in banned:
        dict[item] += 1

print(dict)

fixed_paragraph_list = filter(lambda x: x not in banned, fixed_paragraph_list)

print(collections.Counter(fixed_paragraph_list).most_common(1)[0][0])



