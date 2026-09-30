class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();
        vector<int> result(2 * n);
        
        for (int i = 0; i < nums.size(); i++) {
            result[i] = nums[i];
        }
        for (int i = 0; i < nums.size(); i++) {
            result[n + i] = nums[i];
        }
        return result;
    }
};