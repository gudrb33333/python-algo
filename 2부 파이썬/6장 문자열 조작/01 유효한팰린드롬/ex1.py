import re

def isPalindrome(s: str) -> bool:
    s = s.lower()

    #정규식으로 불필요한 문자 제거
    s = re.sub('[^a-z0-9]','',s)
    print(s)

    return s == s[::-1] #슬라이싱

ex_str:str = "A man, a plan, a canal: Panama"

print(isPalindrome(ex_str))