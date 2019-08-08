def KCloset(point, k):

	def dist(list):
		x, y = list
		distance = (x**2) + (y**2)
		print(distance)
		return distance


	sorted_point = sorted(point, key=dist)
	print(sorted_point)
	return sorted_point[:k]

point = [[1, 3], [-2, 2]]
print(KCloset(point, 1))
