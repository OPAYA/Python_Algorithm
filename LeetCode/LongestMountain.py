class Solution(object):
    def longestMountain(self, A):

    	"""Return longest mountain in number list
    	>>> Solution().longestMountain([2, 1, 4, 7, 3, 2, 5, 6, 7])
    	5
        """
	N = len(A)
        result = base = 0

        while base < N:
            end = base
            if end + 1 < N and A[end] < A[end + 1]: 
              
                while end+1 < N and A[end] < A[end+1]:

                    end += 1
                    
                if end + 1 < N and A[end] > A[end + 1]: 
                  
                    while end+1 < N and A[end] > A[end+1]:
                        end += 1
                        
                    result = max(result, end - base + 1)

            base = max(end, base + 1)
         
        return result

if __name__ == '__main__':
	import doctest
	doctest.testmod()
