class Solution(object):
    def isValid(self, s):
        stack = deque()
        for i in range(len(s)):
            if (s[i] == "(" or s[i] == "[" or s[i] == "{"):
                stack.append(s[i])
            elif (len(stack) > 0):
                if ((s[i] == ')' and stack[-1] == '(') or (s[i] == ']' and stack[-1] == '[') or (s[i] == '}' and stack[-1] == '{')):
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0
        """
        :type s: str
        :rtype: bool
        """
        