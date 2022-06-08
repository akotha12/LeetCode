class Solution {
public:
    int longestPalindrome(string s) {
        sort(s.begin(), s.end());
        char first = s[0];
        int tempCount = 1;
        bool onlyOne = false;
        int palindrome_length = 0;
        for (int i = 1; i < s.size(); i++) {
            if (s[i] == first) {
                tempCount++;
            }
            else {
                if (tempCount % 2 == 1) {
                    tempCount -= 1;
                    onlyOne = true;
                }
                palindrome_length += tempCount;
                first = s[i];
                tempCount = 1;
            } 
        }
        if (tempCount % 2 == 1) {
            tempCount -= 1;
            onlyOne = true;
        }
        palindrome_length += tempCount;
        if (onlyOne) palindrome_length++;
        return palindrome_length;
    }
};