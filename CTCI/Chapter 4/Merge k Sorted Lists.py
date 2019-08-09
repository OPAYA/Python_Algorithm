

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lists = [[1,4,5],[1,3,4],[2,6]]
        def merge(list1, list2):
        	cur = dump = LinstNode(0)
        	while list1 and list2:
        		if list1.val < list2.val:
        			cur.next = list1
        			cur, list1 = cur.next, list1.next
        		else:
        			cur.next = list2
        			cur, list2 = cur.next, list2.next
        	cur.next = last if list1 else list2
        	return dump.next

        n = len(lists)
        print(n)
        l1 = self.mergeKLists(lists[:n//2])
        l2 = self.mergeKLists(lists[n//2:])
        
        return merge(l1, l2)

solution = Solution()
solution.mergeKLists([[1,4,5],[1,3,4],[2,6]])