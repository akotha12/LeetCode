class Solution {
public:
    bool isPalindrome(string s) {
        deque<char> letters;
        for (int i = 0; i < s.length(); i++) {
            if (isalnum(s[i])) {
                letters.push_back(tolower(s[i]));
            }
        }
        while (letters.size() > 1) {
            if (letters.front() == letters.back()) {
                letters.pop_front();
                letters.pop_back();
            }
            else {
                return false;
            }
        }
        return true;
    }
};