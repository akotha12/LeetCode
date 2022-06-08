class Solution {
public:
    bool isValid(string s) {
        deque<char> left;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
                left.push_front(s[i]);
            }
            if (s[i] == ')') {
                if (left.front() == '(') {
                    left.pop_front();
                }
                else {
                    return false;
                }
            }
            if (s[i] == ']') {
                if (left.front() == '[') {
                    left.pop_front();
                }
                else {
                    return false;
                }
            }
            if (s[i] == '}') {
                if (left.front() == '{') {
                    left.pop_front();
                }
                else {
                    return false;
                }
            }
        }
        if (left.empty()) {return true;}
        return false;
    }
};