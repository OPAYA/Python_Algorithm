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
		
def Return_Kth_to_Last(link):
	"""Return Kth node element
	>>> Return_Kth_to_Last('12345')
	5

	"""
	l_list = LinkedList()
	count = 0

	for i in link:
		l_list.append(i)
	returns = l_list.first()
	for _ in range(l_list.size()-1):
		returns = l_list.next()
	returns = int(returns)
	return returns
	
if __name__ == '__main__':
	import doctest
	doctest.testmod()
	Return_Kth_to_Last('12345')
