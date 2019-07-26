class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []
        pair = {")":"(", "}":"{", "]":"["}

        for item in s:
            if item in pair:
                if not stack or stack[-1] != pair[item]:
                    return False
                stack.pop()
            else:
                stack.append(item)
        return len(stack) == 0