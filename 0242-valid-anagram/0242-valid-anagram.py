class Solution(object):
    def isAnagram(self, s, t):
        s = sorted(s)
        t = sorted(t)
        print(s)
        print(t)
        if s == t:
            return True
        return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        