class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        unordered_map<char, int> cs, ct;
        for (char c: s) {
            cs[c]++;
        }
        for (char c: t) {
            ct[c]++;
        }
        return cs == ct;
    }
};
