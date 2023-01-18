class Solution(object):
    def evalRPN(self, tokens):
        stack = deque()
        for token in tokens:
            if (token.isnumeric() or (token[0] == "-" and len(token) > 1)):
                stack.append(int(token))
            else:
                b, a = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(a+b)
                if token == "-":
                    stack.append(a-b)
                if token == "*":
                    stack.append(a*b)
                if token == "/":
                    if (a/b < 0) :
                        stack.append(math.ceil(float(a)/float(b)))
                    else:
                        stack.append(a//b)
        return int(stack[0])       
        
        """
        :type tokens: List[str]
        :rtype: int
        """
        