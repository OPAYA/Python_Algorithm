# def One_away(string1, string2):
# 	if len(string1) == len(string2):


def Check_string(string1, string2):
	check = False
	for ch1, ch2 in zip(string1, string2):
		print(ch1, ch2)
		if ch1 != ch2:
			print('ok')
			if check:
				return False
			check = True
	return True

print(Check_string('ple', 'pale'))