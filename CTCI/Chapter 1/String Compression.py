import doctest

def Compression(string):
	"""Return th compression string of string
	
	>>> Compression('aabbbbcccc')
	a2b4c3
	"""
	val_check=[]
	count = 1
	for i, char in enumerate(string):
		if i== 0:
			b_val = char
		else:
			if char == b_val:
				count = count + 1

			else:
				check = b_val+str(count)
				val_check.append(check)
				b_val = char
				count = 0
	check = b_val+str(count)
	val_check.append(check)
	return "".join(val_check)

print(Compression('aabbbbcccc'))