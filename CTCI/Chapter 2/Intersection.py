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

def Intersection(list1, list2):
	l_list1 = LinkedList()
	l_list2 = LinkedList()
	

	for val1, val2 in zip(list1, list2):
		l_list1.append(val1)
		l_list2.append(val2)

	val1 = l_list1.first()
	val2 = l_list2.first()

	check = False
	for _ in range(len(list1)):
		
		if val1 == val2:
			return True
		else:
			check = False
		val1 = l_list1.next()
		val2 = l_list2.next()
	return check

if __name__ == '__main__':
	list1 = [1,2,4,6,7]
	list2 = [6,7,3,9,0]
	
	print(Intersection(list1, list2))
