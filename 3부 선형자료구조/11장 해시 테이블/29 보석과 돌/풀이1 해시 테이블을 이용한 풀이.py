J = "aA" 
S = "aAAbbbb"

freqs = {}
result = 0

for char in S:
    if char not in freqs:
        freqs[char] = 1
    elif char in freqs:
        freqs[char] += 1

for char in J:
    if char in freqs:
        result += freqs[char]

print(result)