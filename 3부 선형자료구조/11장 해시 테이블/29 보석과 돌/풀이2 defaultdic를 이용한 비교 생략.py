import collections


J = "aA" 
S = "aAAbbbb"

freqs = collections.defaultdict(lambda: 0)
result = 0

for char in S:
    freqs[char] += 1

print(freqs)

for char in J:
    result += freqs[char]

print(result)