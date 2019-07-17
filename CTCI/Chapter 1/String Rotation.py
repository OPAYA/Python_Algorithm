
def Rotation(string):
	"""Return the Rotation string of string

	>>> Rotation('asdfzxcv')
	'vcxzfdsa'
	"""
	length = len(string)
	inverse = []
	for i in range(1, length+1):
		inverse.append(string[length-i])
	return "".join(inverse)

if __name__ == '__main__':
	import doctest
	doctest.testmod()
