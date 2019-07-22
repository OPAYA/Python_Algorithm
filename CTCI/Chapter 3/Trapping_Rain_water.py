class Solution(object):
	def trap(self, heights):

		if not height or len(height) < 3:
			return 0
			
		size = len(heights)
		left = [0] * size
		right = [0] * size

		h = heights[0]
		for i in range(size):
			left[i] = h = max(h, heights[i])

		h = heights[size-1]
		for i in reversed(range(size)):
			right[i] = h = max(h, heights[i])
		print(left)
		print(right)
		print(heights)
		water = 0
		for i in range(size):
			water += min(left[i], right[i]) - heights[i]

		return water

Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])


