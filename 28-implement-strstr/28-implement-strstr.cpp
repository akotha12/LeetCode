class Solution {
public:
    int strStr(string haystack, string needle) {
        char first_letter = needle[0];
        int first = 0;
        string temp;
        for (int i = 0; i < haystack.length(); i++) {
            if (haystack[i] == first_letter) {
                temp = haystack.substr(i, needle.length());
                if (temp == needle) {
                    return i;
                }
            }
        }
        return -1;
    }
};