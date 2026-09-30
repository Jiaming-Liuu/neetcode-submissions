class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> hashmap;
        for (string str: strs) {
            string ordered = str;
            sort(ordered.begin(), ordered.end());
            hashmap[ordered].push_back(str);
        }
        vector<vector<string>> result;
        for (pair p: hashmap) {
            result.push_back(p.second);
        }
        return result;
    }
};
