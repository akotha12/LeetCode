class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        score_stack = []
        
        for o in operations:

            if o == "+" and len(score_stack) >= 2:
                summed = score_stack[-2] + score_stack[-1]
                score_stack.append(summed)
                
            elif o == "D" and len(score_stack) >= 1:
                doubled = score_stack[-1] * 2
                score_stack.append(doubled)
                
            elif o == "C" and len(score_stack) >= 1:
                score_stack.pop() 
                
            else: 
                score_stack.append(int(o))

        return sum(score_stack)
        