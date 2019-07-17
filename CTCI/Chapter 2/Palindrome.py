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
if __name__ == '__main__':
	l_list = LinkedList()
	input = [1, 2, 3, 4, 1]
	for i in input:
		l_list.append(i)

	half_1 = []
	half_2 = []

	fir = l_list.first()
	length = l_list.size()//2
	for j in range(1, l_list.size()+1):
		
		if j== 1:
			half_1.append(l_list.first())
		if j < length:
			half_1.append(l_list.next())
		elif j > length:
			half_2.append(l_list.next())

	check = False	
	for k in range(len(half_1)):
		
		if half_1[k] == half_2[len(half_2)-1-k]:
			check = True
		else:
			check = False

	print(check)
