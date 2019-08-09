class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
		
		dic = {}

		for idx, word in enumerate(words):
			dic[word] = idx

		result = set()
		for idx, word in enumerate(words):
			for j in range(len(word)+1):
				prefix = word[:j]
				reverse_prefix = prefix[::-1]
				suffix = word[j:]
				reverse_suffix = suffix[::-1]
				
				if prefix == reverse_prefix and reverse_suffix in dic:
					rev_idx = dic[reverse_suffix]
					if rev_idx != idx:
						result.add((rev_idx, idx))

				if suffix == reverse_suffix and reverse_prefix in dic:
					rev_idx = dic[reverse_prefix]
					if rev_idx != idx:
						result.add((idx, rev_idx))
		return result

solution = Solution()
print(solution.palindromePairs(["abcd","dcba","lls","s","sssll"]))