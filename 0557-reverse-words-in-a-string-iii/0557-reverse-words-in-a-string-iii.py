class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        output = ""
        for word in s.split():
            output += word[::-1]
            output += " "
        length = len(output) - 1
        return output[0:length]
        