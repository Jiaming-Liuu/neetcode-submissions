class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> temp_m;
        for (int num: nums) {
            temp_m[num]++;
        }
        unordered_map<int, int> m;
        for (auto [key, count]:temp_m) {
            m[count] = key;
        }
        vector<int> result;
        for (int freq = nums.size(); freq >= 1 && result.size() < k; freq--) {
            if (m.count(freq)) {
                result.push_back(m[freq]);
                if (result.size() == k) {
                    break;
                }
            }
        }
        return result;
    }
};
