class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        for (int i = 1; i <= strs[0].size(); i++) {
            string cur_str = strs[0].substr(0, i);
            for (string str:strs) {
                if (str.size() < i or str.substr(0, i) != cur_str) {
                    return str.substr(0, i - 1);
                }
            }
        }
        return strs[0];
    }
};