s = "avvcbdressfdqwe"

used = {}
max_length = 0
start = 0

for index, char in enumerate(s):
    if char in used:
        start = used[char] + 1
    else:
        max_length = max(max_length, index - start + 1)

    used[char] = index

