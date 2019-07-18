class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def __str__(self):
		return str(self.value)

class LinkedList:
	def __init__(self):
		dummy = Node('dummy')
		self.head = dummy
		self.tail = dummy

		self.current = None
		self.before = None

		self.num_of_data = 0

	def append(self, data):
		new_node = Node(data)
		self.tail.next = new_node
		self.tail = new_node

		self.num_of_data += 1

	def delete(self):
		pop_data = self.current.data

		if self.current is self.tail:
			self.tail = self.before

		self.before.next = self.current.next
		self.current = self.before

		self.num_of_data -= 1

		return pop_data

	def first(self):
		if self.num_of_data == 0:
			return None

		self.before = self.head
		self.current = self.head.next

		return self.current.data

	def next(self):
		if self.current.next == None:
			return None

		self.before = self.current
		self.current = self.current.next

		return self.current.data

	def size(self):
		return self.num_of_data


def Sum_list(input_1, input_2):
	"""Return Sum_list
	Sum_list([7, 1, 6], [5, 9, 2])
	912
	"""
	l_list_1 = LinkedList()
	l_list_2 = LinkedList()
	l_list_result = LinkedList()

	for i in input_1:
		l_list_1.append(i)

	for j in input_2:
		l_list_2.append(j)

	while True:
		for i in range(l_list_1.size()):
			if i == 0:
				value1, value2 = l_list_1.first(), l_list_2.first()
				value = value1+value2
				fir_val = value // 10
				value = value % 10
				
				
			else:
				value1, value2 = l_list_1.next(), l_list_2.next()
				value = value1 + value2
				value = value + fir_val
				
				fir_val = value // 10
				value = value % 10 
				
			l_list_result.append(value)
		break
if __name__ == '__main__':
	import doctest
	doctest.testmod()
	input_1 = [7,1,6]
	input_2 = [5, 9, 2]





