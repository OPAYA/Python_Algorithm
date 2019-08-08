from random import choice

class RandomizedSet:
	def __init__(self):
		self.d = {}
		self.l = []

	def insert(self, val):
		if val in self.d:
			return False
		
		self.d[val] = len(self.l)
		
		return True

	def remove(self, val):
		if not val in self.d:
			return False
		self.d.pop(val)

		return True

	def getRandom(self):
		return choice(list(self.d.keys()))

random = RandomizedSet()
print(random.insert(1))
print(random.insert(1))

random.insert(2)
random.insert(3)
random.insert(4)
random.insert(5)
print(random.remove(3))
print(random.remove(3))
print(random.getRandom())