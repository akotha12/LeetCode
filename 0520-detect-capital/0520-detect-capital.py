class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        firstLetterCap = word[0].isupper()
        capCount = 0
        charCount = len(word)
        for char in word:
            if char.isupper():
                capCount += 1
        if capCount == charCount:
            return True
        elif capCount == 0:
            return True
        elif capCount == 1 and firstLetterCap == True:
            return True
        return False
        