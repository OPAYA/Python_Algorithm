class Solution(object):
    def findMaxLength(self, nums):
        """
        >>> Solution().findMaxLength([0, 1, 0, 1])
        2
        >>> Solution().findMaxLength([0, 1, 0])
        2
        
        """
        result = len(set(nums))

        return result

if __name__ == '__main__':
	import doctest
	doctest.testmod()