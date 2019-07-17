def check(string):
	char_set = [0 for _ in range(128)]
	for char in string:
		val = ord(char)
		if char_set[val] == 1:
			return 0
		char_set[val] = 1

	return 1

if __name__ == "__main__":
	UniqueV = check('asdfa')
	 
