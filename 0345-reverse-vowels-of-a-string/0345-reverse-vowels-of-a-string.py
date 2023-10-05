class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        left = 0
        right = len(s) - 1
        if len(s) == 1:
            return s
        characters = list(s)
        while left < right:
            if characters[left] in vowels and characters[right] in vowels:
                characters[left], characters[right] = characters[right], characters[left]
                left += 1
                right -= 1
            elif characters[left] in vowels:
                right -= 1
            elif characters[right] in vowels:
                left += 1
            else:
                left += 1
                right -= 1
        return "".join(characters)