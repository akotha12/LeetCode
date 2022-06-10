class Solution {
public:
    int countPrefixes(vector<string>& words, string s) {
        int total = 0;
        string temp;
        map<int, string> prefixes;
        for (int i = 0; i < s.size(); i++) {
            temp.push_back(s[i]);
            prefixes[i + 1] = temp;
        }
        for (int i = 0; i < words.size(); i++) {
            if (prefixes[words[i].length()] == words[i]) {
                total++;
            }
        }
        return total;
    }
};