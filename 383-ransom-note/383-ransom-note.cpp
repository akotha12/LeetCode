class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        map<char, int> avaliable;
        for (int i = 0; i < magazine.size(); i++) {
            if (avaliable.find(magazine[i]) != avaliable.end()) {
                avaliable[magazine[i]]++;
            }
            else {
                avaliable[magazine[i]] = 1;
            }
        }
        for (int i = 0; i < ransomNote.size(); i++) {
            if (avaliable[ransomNote[i]] > 0) {
                avaliable[ransomNote[i]]--;
            }
            else {
                return false;
            }
        }
        return true;
    }
};