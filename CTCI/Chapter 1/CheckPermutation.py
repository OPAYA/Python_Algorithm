from collections import Counter

def check_per(str1, str2):
	if len(str1) != len(str2)
		return False

		counter = Counter()
		for c in str1:
			counter[c] += 1
		for c in str2:
			if counter[c] == 0:
				return False
			counter[c] -= 1
		return True
if __name__ == '__main__':
	check_per('asdf','fasd')