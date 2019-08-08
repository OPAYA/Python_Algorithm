class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        nums.sort(reverse=True)
        
        return nums[k-1]
solution = Solution()
print(solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4))