words = ["abcd","dcba","lls","s","sssll"]

table = {}

for idx, word in enumerate(words):
	table[word] = idx

res = set()
for idx, word in enumerate(words):
	for j in range(len(word)+1):
		prefix = word[:j]
		reverse_prefix = prefix[::-1]

		suffix = word[j:]
		reverse_suffix = suffix[::-1]
		
		if prefix == reverse_prefix and reverse_suffix in table:
			
			rev_idx = table[reverse_suffix]
			
			if rev_idx != idx:
				res.add((rev_idx, idx))

		if suffix == reverse_suffix and reverse_prefix in table:
			rev_idx = table[reverse_prefix]
			if rev_idx != idx:
				res.add((idx, rev_idx))


print(res)