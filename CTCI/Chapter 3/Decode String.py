class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        for value in s:
            if value == "]":
                tmp, ite, i = [], 0, 0
                while stack[-1] != "[":
                    tmp.append(stack.pop())
                stack.pop()

                while stack and stack[-1].isdigit():
                    ite += int(stack.pop()) *10 **i 
                    i+=1
                stack += tmp[::-1] * ite
            else:
                stack.append(value)
        return "".join(stack)