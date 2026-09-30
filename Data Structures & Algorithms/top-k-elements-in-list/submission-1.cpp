class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> temp_m;
        for (int num: nums) {
            temp_m[num]++;
        }
        unordered_map<int, vector<int>> m;
        for (auto [key, count]:temp_m) {
            m[count].push_back(key);
        }
        vector<int> result;
        for (int freq = nums.size(); freq >= 1 && result.size() < k; freq--) {
            if (m.count(freq)) {
                for (int num: m[freq]) {
                    result.push_back(num);
                }
                if (result.size() == k) {
                    break;
                }
            }
        }
        return result;
    }
};
