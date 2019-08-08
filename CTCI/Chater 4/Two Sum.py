class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        residual = {}
        for i, val in enumerate(nums):
        	

            if val in residual:
            	
                return [residual[val], i]
            residual[target - val] = i
            
        return []

solution = Solution()
print(solution.twoSum([-1, 2, 3, 4, 1], 7))